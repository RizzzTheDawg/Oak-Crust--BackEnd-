from repositories.order_repo import OrderRepo
from models.order_model import Order,OrderRequest,OrderResponse

class OrderService:
    def __init__(self):
        self.repo = OrderRepo()
    def get_all_orders(self):
        return self.repo.get_all()
    def get_by_id_order(self,order_id):
        return self.repo.get_by_id(order_id)
    def create_order(self,data):
        order = OrderRequest(data)
        result = self.repo.create(order)
        return self.repo.get_orders(result)
    def update_order(self,id,data):
        data["ID"] = id
        order = OrderRequest(data)
        self.repo.update(order)
        return self.repo.get_by_id(id)
    def delete_order(self,id):
        print("service working")
        return self.repo.delete(id)
