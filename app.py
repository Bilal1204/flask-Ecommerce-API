from flask import Flask
from flask_restful import Api
from products import Product, ProductList
from cartItems import CartList, CartItem

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<int:id>')
api.add_resource(CartList, '/cart')
api.add_resource(CartItem, '/cart/<int:id>')


if __name__ == "__main__":
    app.run(port=5000, debug=True)