from flask import Blueprint, jsonify, request
from app import db
from app.models import Item

api_bp = Blueprint('api', __name__)

@api_bp.route('/items', methods=['GET'])
def get_items():
    # 商品一覧を取得
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@api_bp.route('/items', methods=['POST'])
def create_item():
    # 商品を作成
    data = request.get_json()
    item = Item(name=data['name'], price=data['price'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@api_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # 特定の商品を取得
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())
