from db_config import get_connection
from models.order_model import Order,OrderRequest,OrderResponse

class OrderRepo:
    def get_all(self):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                SELECT ORD.*,PRD.Product_Name FROM `order` AS ORD
                INNER JOIN product AS PRD ON ORD.Product_ID=PRD.Product_ID;
            """
            cursor.execute(query)
            result=cursor.fetchall()
            return [OrderResponse(row) for row in result]
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def get_by_id(self,id):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                SELECT ORD.*,PRD.Product_Name FROM `order` AS ORD
                INNER JOIN product AS PRD ON ORD.Product_ID=PRD.Product_ID
                WHERE ORD.ID=%s;
            """
            cursor.execute(query,(id,))
            result=cursor.fetchone()
            return OrderResponse(result) if result else None
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def create(self,request: OrderRequest):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                INSERT INTO `order` (Order_ID, Product_ID, Quantity)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (request.Order_ID, request.Product_ID, request.Quantity,))
            connection.commit()
            return request.Order_ID
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def get_orders(self,id):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                SELECT ORD.*,PRD.Product_Name FROM `order` AS ORD
                INNER JOIN product AS PRD ON ORD.Product_ID=PRD.Product_ID
                WHERE ORD.Order_ID= %s
            """
            cursor.execute(query,(id,))
            result=cursor.fetchall()
            return [OrderResponse(row) for row in result]
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def update(self,request: OrderRequest):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                UPDATE `order` AS ORD
                SET ORD.Quantity=%s,ORD.Product_ID=%s, ORD.Order_ID=%s
                WHERE ORD.ID=%s;
            """
            cursor.execute(query,(request.Quantity,request.Product_ID, request.Order_ID,request.ID,))
            connection.commit()
            return request.ID
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
    def delete(self,id):
        connection=get_connection()
        cursor=connection.cursor()
        try:
            query="""
                DELETE FROM `order` 
                WHERE Order_ID = %s;
            """
            cursor.execute(query,(id,))
            connection.commit()
            return "Delete successfully"
        except Exception as e:
            return []
        finally:
            if cursor: cursor.close()
            if connection: connection.close()