from os.path import abspath
import sys
sys.path.append("./model")
from common import Category, Document

class CategoryDTO:
    def __init__(self, category_model: Category) -> None:
        self.id = category_model.id_
        self.name = category_model.name
        self.docs = category_model.docs
        self.created_at = category_model.created_at
        
    def get(self):
        return {
            "id":self.id,
            "name":self.name,
            "docs":self.docs,
            "created_at":self.created_at
        }
    
class DocumentDTO:
    def __init__(self, document_model: Document) -> None:
        self.id = document_model.id_
        self.title = document_model.title
        self.category = document_model.category
        self.author_id = document_model.author_id
        self.created_at = document_model.created_at
        self.meta = document_model.metadata
        
    def get(self):
        return {
            "id":self.id,
            "title":self.title,
            "category":self.category,
            "created_at":self.created_at,
            "metadata":self.meta,
            "author_id":self.author_id
        }
    
    
