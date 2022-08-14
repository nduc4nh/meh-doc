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
    
    def get_all_categroy(self):
        pass
    
    def get_category(self, category_id):
        data = self.repo.get_by_id(category_id)
        return CategoryDTO(Category(data))
        
    def create_category(self, data):
        return self.repo.create(CategoryDTO(Category(data)))
    
    def update_category(self, category_id, data):
        return self.repo.update_by_id(category_id, CategoryDTO(Category(data)))
    
    def delete_category(self):
        return super().delete_category()