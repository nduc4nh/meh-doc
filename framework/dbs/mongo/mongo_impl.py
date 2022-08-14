import logging
from model.dtos import CategoryDTO, DocumentDTO
from model.common import Category, Document
from utils.validators import ModelValidator
from repositories.common import CategoryRepoInteface, DocRepoInteface
from jproperties import Properties
from pymongo import MongoClient
import rsa
import binascii
from os.path import abspath
import sys
sys.path.append(abspath("./"))
# print(abspath("./"))


PATH = abspath("../")


def get_mongo_cred():
    global PATH
    config = Properties()
    with open("framework/dbs/config.properties", "rb") as props:
        config.load(props)
        data = {
            "uri": config.get("mongo_db_endpoint").data.replace(r'"', ""),
            "encripted_password": config.get("mongo_encript_password").data.replace(r'"', ""),
            "username": config.get("mongo_username").data.replace(r'"', "")
        }

    with open("framework/dbs/.secret") as f:
        pv = []
        for line in f:
            pv.append(line)
        pv = pv[0]
    print(data)
    encrypted_password = binascii.unhexlify(
        data['encripted_password'].encode())

    # Process private key
    pv = list(map(int, pv.split(",")))
    plain_password = rsa.decrypt(
        encrypted_password, rsa.PrivateKey(*pv)).decode()

    return data['uri'].replace("<password>", plain_password)


class MongoDocRepoImpl(DocRepoInteface):
    def __init__(self):
        try:
            self.mongo_cred_connect = get_mongo_cred()
            self.mongo_service = MongoClient(self.mongo_cred_connect)
            self.category_repo = self.mongo_service.get_database(
                "meh-doc")["documents"]
        except:
            pass

    # If this class is created check if there's an existing one and use this instance
    def __new__(cls, _cache={}):
        try:
            return _cache["doc_impl"]
        except:
            instance = super(MongoDocRepoImpl, cls).__new__(cls)
            instance.__init__()
            _cache["doc_impl"] = instance
            return instance

    def __del__(self):
        try:
            self.mongo_service.close()
        except:
            pass

    def create(self):
        return super().create()

    def update_by_id(self, id_, data):
        return super().update_by_id(id_, data)

    def get_by_id(self, id_):
        return super().get_by_id(id_)

    def delete_by_id(self):
        pass

    def get_all_docs_by_cate_cate_id(self, cate_id):
        return super().get_all_docs_by_cate_cate_id(cate_id)

    def get_doc_by_title(self, title):
        return super().get_doc_by_title(title)

    def get_all_docs_by_cate_name(self, cate_name):
        return super().get_all_docs_by_cate_name(cate_name)

    def delete_by_id(self, id_):
        return super().delete_by_id(id_)


class MongoCategoryRepoImpl(CategoryRepoInteface):
    def __init__(self):
        self.model_validator = ModelValidator()
        self.mongo_cred_connect = get_mongo_cred()
        self.mongo_service = MongoClient(self.mongo_cred_connect)
        self.category_repo = self.mongo_service.get_database(
            "meh-doc")["categories"]

    # If this class is created check if there's an existing one and use this instance

    def __new__(cls, _cache={}):
        try:
            return _cache["cate_impl"]
        except:
            instance = super(MongoCategoryRepoImpl, cls).__new__(cls)
            instance.__init__()
            _cache["cate_impl"] = instance
            return instance

    def __del__(self):
        try:
            self.mongo_service.close()
        except:
            pass

    def _fetch(self, resp):
        return list(resp)[0]

    def create(self, data: CategoryDTO):
        mongo_doc = data.get()
        print(mongo_doc)
        if not self.model_validator.check_category_model(mongo_doc):
            raise Exception("model invalid")

        self.category_repo.insert_one(mongo_doc)
        return mongo_doc

    def update_by_id(self, id, data: CategoryDTO):
        mongo_doc = data.get()
        if not self.model_validator.check_category_model(mongo_doc):
            raise Exception("model invalid")
        self.category_repo.update_one(
            {"id": id}, {"$set": mongo_doc}, upsert=True)
        return mongo_doc

    def get_by_id(self, id):
        return self._fetch(self.category_repo.find({"id": id}))

    def delete_by_id(self, id):
        self.category_repo.delete_one({"id": id})

    def delete_category_by_name(self, name):
        self.category_repo.delete_one({"name": name})

    def get_category_by_name(self, name):
        return self._fetch(self.category_repo.find({"name": name}))
