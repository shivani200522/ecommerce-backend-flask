from flask import Blueprint, request, jsonify
from database.db import db
from models.user import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
import logging


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    # NOTE: Passwords are hashed using werkzeug for security
    password = generate_password_hash(data.get("password"))
    role = data.get("role")

    if not username or not password or not role:
        return jsonify({"error": "Missing fields"}), 400

    # check if user exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # create new user
    new_user = User(
        username=username,
        password=password,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User registered successfully"
    }), 201



import logging
from werkzeug.security import check_password_hash
from flask import request

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    # ✅ SAFE CHECK
    if not data or "username" not in data or "password" not in data:
        logging.warning("Login attempt with missing fields")
        return {"message": "Missing username or password"}, 400

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        logging.warning(f"Failed login attempt for username: {data.get('username')}")
        return {"message": "Invalid credentials"}, 401

    access_token = create_access_token(identity=str(user.id))

    logging.info(f"User logged in: {user.username}")

    return {
        "message": "Login successful",
        "token": access_token
    }