import json
from flask import Blueprint,request,jsonify

from services.order_service import OrderService

order_bp = Blueprint ('order_bp', __name__)

service=OrderService()

@order_bp.route('/order',methods=['GET'])
def get_all ():
    products = service.get_all_orders()
    return jsonify([vars(p) for p in products])

@order_bp.route('/order/<int:order_id>',methods=['GET'])
def get_by_id(order_id):
    product = service.get_by_id_order(order_id)
    if product:
        return jsonify(vars(product))
    return jsonify({'error': 'Product not found'}), 404

@order_bp.route('/order', methods=['POST'])
def create():
    try:
        data = request.get_json()
        order = service.create_order(data)
        if order:
            return jsonify([vars(row) for row in order]),201
        else:
            return jsonify({'error': 'Something went wrong'}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@order_bp.route('/order/<int:id>',methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        order = service.update_order(id,data)
        if order:
            return jsonify(vars(order)),200
        else:
            return jsonify({'error': 'Something went wrong'}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@order_bp.route('/order/<int:Order_ID>',methods=['DELETE'])
def delete(Order_ID):
    try:
        order = service.delete_order(Order_ID)
        if order:
            return jsonify(order),200
        else:
            return jsonify({'error': 'Something went wrong'}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
