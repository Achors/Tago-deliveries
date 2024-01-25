from flask_restful import Resource, reqparse
from models import db, Product
from .schema import ProductSchema
from flask import jsonify

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return jsonify(product_schema.dump(product))

    def put(self, product_id):
        product = Product.query.get_or_404(product_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('price', type=float)
        args = parser.parse_args()


        product.name = args['name'] or product.name
        product.price = args['price'] or product.price

        db.session.commit()
        return jsonify(product_schema.dump(product))

    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204

class ProductsResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify(products_schema.dump(products, many=True))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        args = parser.parse_args()

        new_product = Product(
            name=args['name'],
            price=args['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
