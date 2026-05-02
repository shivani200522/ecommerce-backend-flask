# Digital Product Marketplace API

## Description
A REST API built using Flask for a digital product marketplace where users can register, login, upload products, and purchase them.

## Features
- User Authentication (Register/Login)
- Product Management (Add/View)
- Order System (Purchase/View Orders)

## Tech Stack
- Flask
- SQLite
- SQLAlchemy

## API Endpoints

### Auth
POST /register  
POST /login  

### Products
POST /add-product  
GET /products  

### Orders
POST /create-order  
GET /orders/<user_id>  

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run server:
python app.py