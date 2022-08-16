from os.path import abspath
import sys
sys.path.append(abspath("./"))
from service.common import Service
from framework.dbs.mongo.mongo_impl import MongoCategoryRepoImpl
from model.common import Category, CategoryDTO
from uuid import uuid4
import time

class CategoryService(Service):
    def __init__(self) -> None:
        self.repo = MongoCategoryRepoImpl()
    
    def get_all_category(self, page):
        return self.repo.get_all_category_page(page)
    
    def get_category(self, category_id:str):
        data = self.repo.get_by_id(category_id)
        return CategoryDTO.from_model(data)
        
    def create_category(self, data:CategoryDTO):
        model = Category.from_dto(data)
        model.id_ = uuid4().__str__()
        model.created_at = str(int(time.time()))
        model = self.repo.create(model)
        return CategoryDTO.from_model(model)
    
    def update_category(self, category_id:str, data:CategoryDTO):
        model = self.repo.update_by_id(category_id, Category.from_dto(data))
        return CategoryDTO.from_model(model)
    def delete_category(self, category_id:str):
        return self.repo.delete_by_id(category_id) 
