from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import JSONResponse

from os.path import abspath
import sys
sys.path.append(abspath("./"))
from model.common import  CategoryDTO
from controller.api_common import BasicControllerUI
from framework.fastapi.service_impl import CategoryService
app = FastAPI()
router = InferringRouter()

@cbv(router)
class FastApiController(BasicControllerUI):
    def __init__(self) -> None:
        self.category_service = CategoryService()

    # @router.get("/categories/{cate_name}")
    # def get_category_by_name(self, cate_name):
    #     return super().get_category_by_name(cate_name)
    
    @router.get("/categories/{cate_id}")
    def get_category_by_id(self, cate_id:str):
        response = {
            "data":self.category_service.get_category(cate_id).get()
        }
        return JSONResponse(content=response) 

    @router.get("/categories")
    def get_all_categories(self, page:int = 1):
        data = self.category_service.get_all_category(page)
        response = {
            "data":[CategoryDTO.from_model(ele).get() for ele in data]
        }
        return JSONResponse(content=response)  
    
    @router.post("/categories")
    def create_category(self, data:CategoryDTO):
        print(data)
        response = {
            "data":self.category_service.create_category(data).get()
        }
        return JSONResponse(content=response)  
    
    @router.put("/categories/{cate_id}")
    def update_category_by_id(self, cate_id, data:CategoryDTO):
        response = {
            "data":self.category_service.update_category(cate_id, data).get()
        }
        return JSONResponse(content=response)  
        
    
    @router.delete("/categories")
    def delete_category_by_id(self, cate_id):
        self.category_service.delete_category(cate_id)
        return JSONResponse(content={"data":"ok"})