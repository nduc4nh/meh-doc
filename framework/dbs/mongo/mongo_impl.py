from jproperties import Properties
from pymongo import MongoClient
import rsa
import binascii
import os
import sys
from repositories.common import CategoryRepoInteface, DocRepoInteface

PATH = os.path.abspath("../")


def get_mongo_cred():
    global PATH
    config = Properties()
    with open("{}/config.properties".format(PATH), "rb") as props:
        config.load(props)
        data = {
            "uri": config.get("mongo_db_endpoint"),
            "encripted_password": config.get("mongo_encript_password"),
            "username": config.get("mongo_username")
        }

    with open("{}/.secret") as f:
        pv = []
        for line in f:
            pv.append(line)
        pv = pv[0]

    encrypted_password = binascii.unhexlify(
        data['encripted_password'].encode())
    plain_password = rsa.decrypt(encrypted_password, pv).decode()

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
        try:
            self.mongo_cred_connect = get_mongo_cred()
            self.mongo_service = MongoClient(self.mongo_cred_connect)
            self.category_repo = self.mongo_service.get_database(
                "meh-doc")["categories"]
        except:
            pass

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

    def get_category_by_name(self, name):
        pass

    def get_category_by_name(self, name):
        pass

    def delete_category_by_name(self, name):
        pass
