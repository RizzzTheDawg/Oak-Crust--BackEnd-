from db_config import get_connection
from models.category_model import Category,CategoryRequest,CategoryResponse
from models.product_model import ProductRequest


class CategoryRepo:
    def get_all (self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                SELECT * FROM category
            """
            cursor.execute(query)
            result=cursor.fetchall()
            return [CategoryResponse(row) for row in result]
            #return ProductResponse(row) if row else None
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def get_by_id(self,id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                SELECT * FROM category AS CTG
                WHERE CTG.Category_ID=%s
            """
            cursor.execute(query,(id,))
            result=cursor.fetchone()
            return CategoryResponse(result) if result else None
        except Exception as e:
            return "Item not found"
        finally:
            if cursor: cursor.close()
            if connection: connection.close()

    def creat(self,request: CategoryRequest):
        connection = get_connection()
        cursor=connection.cursor()
        try:
            query = """
                INSERT INTO category (Category_Name) VALUES 
                    (%s)
            """
            cursor.execute(query,(request.Category_Name,))
            connection.commit()
            return "Created Successfully"
        except Exception as e:
            return "Error: could not update"
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def update(self,request: CategoryRequest):
        connection = get_connection()
        cursor=connection.cursor()
        try:
            query = """
                UPDATE category AS CTG
                SET CTG.Category_Name=%s
                WHERE CTG.Category_ID=%s
            """
            cursor.execute(query,(request.Category_Name,request.Category_ID,))
            connection.commit()
            return "Update was successful"
        except Exception as e:
            return "Error: could not update"
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def delete(self,id):
        connection = get_connection()
        cursor=connection.cursor()
        try:
            query = """
                DELETE FROM category
                WHERE Category_ID=%s
            """
            cursor.execute(query,(id,))
            connection.commit()
            return "Delete was successful"
        except Exception as e:
            return "Error: could not delete"
        finally:
            if cursor: cursor.close()
            if connection: connection.close()