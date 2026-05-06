from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database.db import db

from models.user import User
from routes.auth_routes import auth_bp
from models.product import Product

from models.order import Order
from routes.order_routes import order_bp


from routes.product_routes import product_bp

from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(auth_bp)

import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR, "logs", "app.log")

if not os.path.exists(os.path.join(BASE_DIR, "logs")):
    os.mkdir(os.path.join(BASE_DIR, "logs"))

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

db.init_app(app)


app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

@app.route("/")
def home():
    return {"message": "API is running"}

@app.route("/test-log")
def test_log():
    logging.info("TEST LOG WORKING")
    return "Logged!"


if __name__ == "__main__":
    app.run(debug=True)