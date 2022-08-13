from jproperties import Properties
from pymongo import MongoClient
import rsa
import binascii
import os, sys

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
    
    encrypted_password = binascii.unhexlify(data['encripted_password'].encode())
    plain_password = rsa.decrypt(encrypted_password, pv).decode()

    return data['uri'].replace("<password>", plain_password)

class MongoRepoImpl:
    def __init__(self):
        try:
            self.mongo_cred_connect = get_mongo_cred()
            self.MongoRepo = MongoClient(self.mongo_cred_connect)
        except:
            pass