class Product:
    def __init__(self,Category_ID,Price,Product_ID,Product_Name):
        self.Category_ID=Category_ID
        self.Price=Price
        self.Product_ID=Product_ID
        self.Product_Name=Product_Name

class ProductRequest:
    def __init__(self,data):
        self.category_id=data.get('Category_ID')
        self.price=data.get('Price')
        self.product_name=data.get('Product_Name')
        self.Product_ID=data.get('Product_ID')

class ProductResponse:
    def __init__(self,data):
        self.Category_ID=data.get('Category_ID')
        self.Price=data.get('Price')
        self.Product_Name=data.get('Product_Name')
        self.Category_Name=data.get("Category_Name")
        self.Product_ID=data.get('Product_ID')
