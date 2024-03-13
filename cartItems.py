import sqlite3
from flask_restful import Resource, reqparse

db_location = "data.db"

class CartItem(Resource):
    def delete(self, id):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        cursor.execute("DELETE FROM CartItem WHERE product_id=?", (id,))
        db.commit()
        db.close()

        return {'message': 'Cart item deleted'}, 200

class CartList(Resource):
    def get(self):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM CartItem")
        cart_items = cursor.fetchall()

        db.close()

        return {'cart_items': cart_items}, 200
    
    def post(self):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        parser = reqparse.RequestParser()
        parser.add_argument('id', type = int, required = True,
            help = 'No cart Id provided', location = 'json')
        parser.add_argument('product_id', type = int, required = True,
            help = 'No product id provided', location = 'json')
        parser.add_argument('quantity', type = int, required = True,
            help = 'No quantity provided', location = 'json')

        args = parser.parse_args()
        cursor.execute(
            "INSERT INTO CartItem (id, product_id, quantity) VALUES (?, ?, ?)",
            (args['id'], args['product_id'], args['quantity'])
        )
        db.commit()
        db.close()
        return {'message': 'New cart item added'}, 201