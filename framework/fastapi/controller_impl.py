from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from os.path import abspath
import sys
sys.path.append(abspath("./"))
from model.common import Category
from model.dtos import CategoryDTO
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
        return self.category_service.get_category(cate_id)

    @router.get("/categories")
    def get_all_categories(self, page:int = 1):
        data = self.category_service.get_all_category(page)
        return [CategoryDTO.from_model(ele) for ele in data]
    
    @router.post("/categories")
    def create_category(self, data:CategoryDTO):
        return self.category_service.create_category(data)
    
    @router.put("/categories/{cate_id}")
    def update_category_by_id(self, cate_id, data:CategoryDTO):
        return [self.category_service.update_category(cate_id, data)]
    
    @router.delete("/categories")
    def delete_category_by_id(self, cate_id):
        self.category_service.delete_category(cate_id)