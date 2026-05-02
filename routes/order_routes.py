from flask import Blueprint, request, jsonify
from database.db import db
from models.order import Order
from models.product import Product
from models.user import User

order_bp = Blueprint("order", __name__)

@order_bp.route("/create-order", methods=["POST"])
def create_order():
    data = request.get_json()

    user_id = data.get("user_id")
    product_id = data.get("product_id")

    if not user_id or not product_id:
        return jsonify({"error": "Missing fields"}), 400

    user = User.query.get(user_id)
    product = Product.query.get(product_id)

    if not user or user.role != "buyer":
        return jsonify({"error": "Invalid buyer"}), 400

    if not product:
        return jsonify({"error": "Product not found"}), 404

    order = Order(
        user_id=user_id,
        product_id=product_id
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"})


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