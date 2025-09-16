class Category:
    def __init__(self, Category_ID, Category_Name):
        self.Category_ID = Category_ID
        self.Category_Name = Category_Name


class CategoryRequest:
    def __init__(self, data):
        self.Category_ID = data.get("Category_ID")
        self.Category_Name = data.get("Category_Name")


class CategoryResponse:
    def __init__(self, data):
        self.Category_ID = data.get("Category_ID")
        self.Category_Name = data.get("Category_Name")
