from database.db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    file_url = db.Column(db.Text, nullable=False)

    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)