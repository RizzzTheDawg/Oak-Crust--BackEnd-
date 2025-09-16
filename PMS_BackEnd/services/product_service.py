from repositories.product_repo import ProductRepo
from models.product_model import Product,ProductRequest,ProductResponse

class ProductService:
    def __init__(self):
        self.repo=ProductRepo()
    def get_all_product(self):
        return self.repo.get_all()
    def get_by_id_product(self,id):
        return self.repo.get_by_id(id)
    def create_product(self,request):
        data=ProductRequest(request)
        id=self.repo.create(data)
        return self.repo.get_by_id(id)
    def update_product(self,id,request):
        data=ProductRequest(request)
        data.Product_ID=id
        self.repo.update(data)
        return self.repo.get_by_id(id)
    def delete_product(self,id):
        return self.repo.delete(id)