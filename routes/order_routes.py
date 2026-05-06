from flask import Blueprint, request, jsonify
from database.db import db
from models.order import Order
from models.product import Product
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
import logging

order_bp = Blueprint("order", __name__)

@order_bp.route("/create-order", methods=["POST"])
@jwt_required()
def create_order():
    data = request.json

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role != "buyer":
        return {"message": "Only buyers can place orders"}, 403

    new_order = Order(
        user_id=user.id,
        product_id=data["product_id"]
    )

    db.session.add(new_order)
    db.session.commit()
    logging.info(f"Order placed by user {user.id} for product {data['product_id']}")

    return {"message": "Order placed successfully"}


@order_bp.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()

    result = []
    for o in orders:
        result.append({
            "order_id": o.id,
            "product_id": o.product_id,
            "date": str(o.created_at)
        })

    return jsonify(result)

@order_bp.route("/all-orders", methods=["GET"])
def all_orders():
    orders = Order.query.all()

    return [
        {
            "order_id": o.id,
            "user_id": o.user_id,
            "product_id": o.product_id
        }
        for o in orders
    ]