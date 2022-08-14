from os.path import abspath 
import sys
sys.path.append(abspath("./utils"))
from utils.logger import log

class ModelValidator:

    def _valid_field(self, inp:list, data:dict):
        
        try:
            for field in data.keys():
                assert(field in inp)
        except: return False
        return True
    
    def _check_schema(self, data:dict, shemap:dict):
        for field, type_ in shemap.items():
            if type(data[field]) != type_:
                return False
        return True

    def check_document_model(self, model:dict):
        if not self._valid_field(["id", "title", "category", "author_id", "created_at", "meta"], model):
            return False

        if not self._check_schema(model, {
            "id":str,
            "title":str,
            "category":dict,
            "author_id":str,
            "created_at":str,
            "meta":str
        }): return False

        if not model["category"]:
            return False

        return True
    
    def check_category_model(self, model:dict):
        log("check category fields")
        if not self._valid_field(["id", "name", "created_at", "docs"], model ):
            return False
        log("check category schema")
        
        if not self._check_schema(model, {
            "id":str,
            "name":str,
            "created_at":str,
            "docs":list
        }): return False

        return True
