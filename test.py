# from mongo_impl import MongoCategoryRepoImpl
# from model.dtos import CategoryDTO
# from model.common import Category
# import time

# repo = MongoCategoryRepoImpl()
# cate = Category({
#     "id":"1",
#     "name":"test2",
#     "created_at":str(int(time.time())),
#     "docs":[]
# })
# cate_dto = CategoryDTO(cate)
# # repo.create(cate_dto)
    
# print(repo.get_category_by_name("test2"))

from os.path import abspath
import sys

sys.path.append(abspath("./"))
from framework.fastapi.controller_impl import app, router
app.include_router(router)