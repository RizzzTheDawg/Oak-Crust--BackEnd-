import json
from flask import Blueprint,request,jsonify

from services.product_service import ProductService

product_bp = Blueprint ('product_bp', __name__)

service=ProductService()

@product_bp.route('/products',methods=['GET'])
def get_all ():
    products = service.get_all_product()
    return jsonify([vars(p) for p in products])

@product_bp.route('/products/<int:product_id>',methods=['GET'])
def get_by_id(product_id):
    product = service.get_by_id_product(product_id)
    if product:
        return jsonify(vars(product))
    return jsonify({'error': 'Product not found'}), 404

@product_bp.route('/products', methods=['POST'])
def create():
    try:
        data = request.get_json()
        product = service.create_product(data)
        if product:
            return jsonify(vars(product)),201
        else:
            return jsonify({'error': 'Something went wrong'}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    product = service.update_product(id,data)
    if product:
        return jsonify(vars(product)),201
    else:
        return jsonify({'error': 'Something went wrong'}), 500
    
@product_bp.route('/products/<int:Product_ID>', methods=['DELETE'])
def delete(Product_ID):
    try:
        service.delete_product(Product_ID)
        return jsonify({"message":"Product deleted"})
    except Exception as e:
        return jsonify({'error': 'Something went wrong'}),500