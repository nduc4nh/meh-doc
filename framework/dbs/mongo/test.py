from mongo_impl import MongoCategoryRepoImpl
from model.dtos import CategoryDTO
from model.common import Category
import time

repo = MongoCategoryRepoImpl()
cate = Category({
    "id":"1",
    "name":"test2",
    "created_at":str(int(time.time())),
    "docs":[]
})
cate_dto = CategoryDTO(cate)
# repo.create(cate_dto)
    
print(repo.get_category_by_name("test2"))
