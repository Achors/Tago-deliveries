from flask_restful import Resource, reqparse
from models import db, Product
from schema import ProductSchema
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
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        # Update product attributes
        product.name = args['name'] or product.name
        product.price = args['price'] or product.price
        product.description = args['description'] or product.description

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
        return jsonify(products_schema.dump(products))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        new_product = Product(
            name=args['name'],
            price=args['price'],
            description=args['description']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(product_schema.dump(new_product)), 201
