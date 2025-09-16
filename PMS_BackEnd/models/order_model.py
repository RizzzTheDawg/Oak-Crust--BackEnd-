class Order:
    def __init__(self,ID,Order_ID,Product_ID,Quantity):
        self.ID=ID
        self.Order_ID=Order_ID
        self.Product_ID=Product_ID
        self.Quantity=Quantity

class OrderRequest:
    def __init__(self,data):
        self.Order_ID=data.get('Order_ID')
        self.Product_ID=data.get('Product_ID')
        self.Quantity=data.get('Quantity')
        self.ID=data.get('ID')

class OrderResponse:
    def __init__(self,data):
        self.Order_ID=data.get('Order_ID')
        self.Product_ID=data.get('Product_ID')
        self.Quantity=data.get('Quantity')
        self.Product_Name=data.get('Product_Name')