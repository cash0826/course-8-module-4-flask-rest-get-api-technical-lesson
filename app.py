# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement a homepage route that returns a JSON welcome message
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Product API", "resource_endpoint": "/products"}), 200

# TODO: Implement GET /products to return all products or filter by category
@app.route('/products', methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200

# TODO: Implement GET /products/<id> to return a single product by ID
@app.route('/products/<int:id>', methods=["GET"])
def get_product(id):
    for product in data:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

# Considerations: real-world apps require a database. 
# Plan to integrate a database or data service to manage large datasets

# Error-handling. Keep in mind what different ways users can hit an endpoints
# Return HTTP status codes and JSON error messages

# Security: GET requests may expose query strings and sensitive data. 
# Avoid placing confidential information in the query

# Inconsistent formatting across endpoints can lead to confusion
# Follow predictable schema for all GET responses and use the same key structure throughout the API