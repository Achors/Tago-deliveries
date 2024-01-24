from flask_restful import Resource, reqparse
from models import db, Store
from schema import StoreSchema
from flask import jsonify

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

class Store(Resource):
    def get(self, store_id):
        store = Store.query.get_or_404(store_id)
        return jsonify(store_schema.dump(store))

    def put(self, store_id):
        store = Store.query.get_or_404(store_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('products', type=str)
        args = parser.parse_args()

        store.name = args['name'] or store.name
        store.location = args['location'] or store.location
        store.products = args['products'] or store.products

        db.session.commit()
        return jsonify(store_schema.dump(store))

    def delete(self, store_id):
        store = Store.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return '', 204

class Stores(Resource):
    def get(self):
        stores = Store.query.all()
        return jsonify(stores_schema.dump(stores))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('location', type=str, required=True)
        parser.add_argument('products', type=str, required=True)
        args = parser.parse_args()

        new_store = Store(name=args['name'], location=args['location'], products=args['products'])
        db.session.add(new_store)
        db.session.commit()
        return jsonify(store_schema.dump(new_store)), 201
