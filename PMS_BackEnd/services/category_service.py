from repositories.category_repo import CategoryRepo
from models.category_model import Category,CategoryRequest,CategoryResponse

class CategoryService:
    def __init__(self):
        self.repo = CategoryRepo()
    def get_all_category(self):
        return self.repo.get_all()
    def get_category_by_id(self,id):
        return self.repo.get_by_id(id)
    def creat_category(self,data):
        data=CategoryRequest(data)
        return self.repo.creat(data)
    def update_category(self,data,id):
        items=CategoryRequest(data)
        items.Category_ID=id
        return self.repo.update(items)
    def delete_category(self,id):
        return self.repo.delete(id)

