import json
from flask import Blueprint,request,jsonify

from services.category_service import CategoryService

category_bp = Blueprint ('category_bp', __name__)

service=CategoryService()

@category_bp.route('/categories',methods=['GET'])
def get_all():
    category=service.get_all_category()
    return jsonify([vars(items) for items in category])

@category_bp.route('/categories/<int:Category_ID>',methods=['GET'])
def get_by_id(Category_ID):
    category=service.get_category_by_id(Category_ID)
    if category:
        return  jsonify(vars(category))
    else:
        return jsonify({'error': 'Category not found'}), 404

@category_bp.route('/categories',methods=['POST'])
def create():
    data=request.get_json()
    category=service.creat_category(data)
    if category:
        return jsonify(category)
    else:
        return jsonify({'error': 'Category could not creat'}), 404

@category_bp.route('/categories/<int:Category_ID>',methods=['PUT'])
def update(Category_ID):
    data=request.get_json()
    category=service.update_category(data,Category_ID)
    if category:
        return jsonify({'message': category})
    else:
        return jsonify({'error': 'Category could not update'}), 404

@category_bp.route('/categories/<int:Category_ID>',methods=['DELETE'])
def delete(Category_ID):
    result=service.delete_category(Category_ID)
    if result:
        return jsonify({'message': result})
    else:
        return jsonify({'error': 'Category could not delete'}), 40444