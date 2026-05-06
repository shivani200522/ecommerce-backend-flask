# 🛒 E-Commerce Backend (Flask)

## 📌 Overview

This is a RESTful E-commerce backend built using Flask.
It supports user authentication, product management, and order processing.

---

## 🚀 Features

* User Registration & Login
* JWT Authentication
* Role-Based Access (Seller / Buyer)
* Product Management
* Order Management
* Logging System

---

## 🛠 Tech Stack

* Python (Flask)
* SQLite
* SQLAlchemy
* JWT (Authentication)

---

## 📂 API Endpoints

### Auth

* POST `/register`
* POST `/login`

### Products

* POST `/add-product` (Seller only)
* GET `/products`

### Orders

* POST `/create-order` (Buyer only)
* GET `/orders`
* GET `/all-orders`

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## 🧪 Testing

Use Postman to test APIs.

---

## 📊 Database

SQLite database managed via SQLAlchemy ORM.

---

## 📜 Logging

Logs stored in `logs/app.log`

---


