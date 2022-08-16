# from os.path import abspath
# import sys
# # sys.path.append(abspath("./"))
# # sys.path.append(abspath("./model"))
# from model.common import Category, Document
# from pydantic import BaseModel
# from typing import List

# class CategoryDTO(BaseModel):
#     # def __init__(self, category_model: Category) -> None:
#     #     self.id = category_model.id_
#     #     self.name = category_model.name
#     #     self.docs = category_model.docs
#     #     self.created_at = category_model.created_at
#     id: str
#     name: str
#     docs: List[dict]
#     created_at: str

#     def get(self):
#         return {
#             "id":self.id,
#             "name":self.name,
#             "docs":self.docs,
#             "created_at":self.created_at
#         }
    
#     @staticmethod
#     def from_model(cate:Category):
#         return CategoryDTO(** cate.to_dict())

    
# class DocumentDTO:
#     def __init__(self, document_model: Document) -> None:
#         self.id = document_model.id_
#         self.title = document_model.title
#         self.category = document_model.category
#         self.author_id = document_model.author_id
#         self.created_at = document_model.created_at
#         self.meta = document_model.metadata
        
#     def get(self):
#         return {
#             "id":self.id,
#             "title":self.title,
#             "category":self.category,
#             "created_at":self.created_at,
#             "metadata":self.meta,
#             "author_id":self.author_id
#         }
    
#     @staticmethod
#     def from_model(doc:Document):
#         return CategoryDTO(** doc.to_dict())
    
    
