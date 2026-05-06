from flask import Blueprint, request, jsonify
from database.db import db
from models.product import Product
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging

product_bp = Blueprint("product", __name__)

@product_bp.route("/add-product", methods=["POST"])
@jwt_required()
def add_product():
    data = request.json

    user_id = get_jwt_identity()

    # 🔥 GET USER FROM DB
    user = User.query.get(user_id)

    if user.role != "seller":
        return {"message": "Only sellers can add products"}, 403

    new_product = Product(
        name=data["name"],
        price=data["price"],
        file_url=data["file_url"],
        seller_id=user.id
    )

    db.session.add(new_product)
    db.session.commit()
    logging.info(f"Product added: {new_product.name} by user {user.id}")

    return {"message": "Product added successfully"}

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price
        }
        for p in products
    ]