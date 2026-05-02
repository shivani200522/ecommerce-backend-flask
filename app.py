from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database.db import db

from models.user import User
from routes.auth_routes import auth_bp
from models.product import Product

from models.order import Order
from routes.order_routes import order_bp


from routes.product_routes import product_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)

db.init_app(app)

app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)