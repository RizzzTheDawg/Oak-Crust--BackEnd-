from db_config import get_connection
from models.product_model import Product,ProductRequest,ProductResponse

class ProductRepo:
    def get_all (self):
        try:
            connection=get_connection()
            cursor= connection.cursor()
            cursor.execute("SELECT PRD.*,CAT.Category_Name FROM product AS PRD " \
            "LEFT JOIN category AS CAT ON CAT.Category_ID=PRD.Category_ID")
            result=cursor.fetchall()
            print(result)
            return [ProductResponse(row) for row in result]
            #return ProductResponse(row) if row else None
        except Exception as e:
            return []
        finally: 
            cursor.close()
            connection.close()
    def get_by_id(self,id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                SELECT PRD.*, CTG.Category_Name 
                FROM product AS PRD
                LEFT JOIN category AS CTG ON CTG.Category_ID = PRD.Category_ID
                WHERE PRD.Product_ID = %s
            """
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            
            return ProductResponse(row) if row else None
        except Exception as e:
            return None
        finally:
            cursor.close()
            connection.close()
    def create(self, request: ProductRequest):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                INSERT INTO product (Category_ID, Price, Product_Name)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (request.category_id, request.price, request.product_name,))
            connection.commit()
            product_id = cursor.lastrowid
            return product_id
        except Exception as e:
            print("Create Error:", e)
            return None
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def update(self,request:ProductRequest):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query= """
                UPDATE product AS PRD
                SET PRD.Price=%s, PRD.Product_Name=%s, PRD.Category_ID=%s
                WHERE PRD.Product_ID=%s
            """
            cursor.execute(query, (request.price,request.product_name,request.category_id,request.Product_ID))
            connection.commit()
            return request.product_id
        except Exception as e:
            print("Update Error:",e)
            return None
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def delete(self,id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query="""
                DELETE FROM product
                WHERE Product_ID = %s
            """
            cursor.execute(query,(id))
            connection.commit()
        except Exception as e:
            print("Delete Error:",e)
            return None
        finally:
            if cursor: cursor.close()
            if connection: connection.close()