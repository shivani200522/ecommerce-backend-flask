from flask import Blueprint, request, jsonify
from database.db import db
from models.product import Product
from models.user import User

product_bp = Blueprint("product", __name__)

@product_bp.route("/add-product", methods=["POST"])
def add_product():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    file_url = data.get("file_url")
    seller_id = data.get("seller_id")

    if not name or not price or not file_url or not seller_id:
        return jsonify({"error": "Missing fields"}), 400

    seller = User.query.get(seller_id)

    if not seller or seller.role != "seller":
        return jsonify({"error": "Invalid seller"}), 400

    product = Product(
        name=name,
        price=price,
        file_url=file_url,
        seller_id=seller_id
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added"})

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "file_url": p.file_url,
            "seller_id": p.seller_id
        })

    return jsonify(result)