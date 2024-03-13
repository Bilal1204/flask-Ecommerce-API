import sqlite3
from flask_restful import Resource, reqparse

db_location = "data.db"


class ProductList(Resource):
    def get(self):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()

        db.close()

        return {'products': products}, 200

    def post(self):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        parser = reqparse.RequestParser()
        parser.add_argument('id', type = int, required = True,
            help = 'No product Id provided', location = 'json')
        parser.add_argument('name', type = str, required = True,
            help = 'No product name provided', location = 'json')
        parser.add_argument('description', type = str, default = "", required = True, location = 'json')
        parser.add_argument('price', type = float, required = True,
            help = 'No product price provided', location = 'json')
        parser.add_argument('image_url', type = str, default = "", required = True, location = 'json')

        args = parser.parse_args()

        try:
            cursor.execute(
                "INSERT INTO Product (id, name, description, price, image_url) VALUES (?, ?, ?, ?, ?)",
                (args['id'], args['name'], args['description'], args['price'], args['image_url'])
            )
        except sqlite3.IntegrityError:
            return {'message': 'A product with id {} already exists'.format(args['id'])}, 400
        
        db.commit()
        db.close()
        return {'message': 'New product added'}, 201
    

class Product(Resource):
    
    def get(self, id):
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM Product WHERE id=?", (id,))
        product = cursor.fetchone()

        db.close()

        if product is None:
            return {'message': 'Product not found'}, 404

        return {'product': product}, 200