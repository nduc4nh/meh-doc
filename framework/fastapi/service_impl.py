from os.path import abspath
import sys
sys.path.append(abspath("./"))
from service.common import Service
from framework.dbs.mongo.mongo_impl import MongoCategoryRepoImpl
from model.common import Category
from model.dtos import CategoryDTO

class CategoryService(Service):
    def __init__(self) -> None:
        self.repo = MongoCategoryRepoImpl()
    
    def get_all_category(self, page):
        return self.repo.get_all_category_page(page)
    
    def get_category(self, category_id:str):
        data = self.repo.get_by_id(category_id)
        return CategoryDTO.from_model(Category(data))
        
    def create_category(self, data:CategoryDTO):
        return self.repo.create(Category.from_dto(data))
    
    def update_category(self, category_id:str, data:CategoryDTO):
        return self.repo.update_by_id(category_id, Category.from_dto(data))
    
    def delete_category(self, category_id:str):
        return self.repo.delete_by_id(category_id) 
