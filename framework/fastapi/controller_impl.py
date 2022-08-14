from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from os.path import abspath
import sys
sys.path.append(abspath("./"))
from controller.api_common import BasicControllerUI

app = FastAPI()
router = InferringRouter()

@cbv(router)
class FastApiController(BasicControllerUI):
    def __init__(self) -> None:
        pass
    
    @router.get("/categories/{cate_name}")
    def get_category_by_name(self, cate_name):
        return super().get_category_by_name(cate_name)
    
    @router.get("/categories/{cate_id}")
    def get_category_by_id(self, cate_id):
        return super().get_category_by_id(cate_id)

    @router.get("/categories")
    def get_all_categories(self):
        return super().get_all_categories()
    
    @router.post("/categories")
    def create_category(self, data):
        return super().create_category(data)
    
    @router.put("/categories/{cate_id}")
    def update_category_by_id(self, cate_id):
        return super().update_category_by_id(cate_id)
    
    @router.delete("/categories")
    def delete_category_by_id(self, cate_id):
        return super().delete_category_by_id(cate_id)