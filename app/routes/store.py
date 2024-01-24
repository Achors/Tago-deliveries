from flask_restful import Resource, reqparse
from .models import db, Store
from .schema import StoreSchema
from flask import jsonify

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

class StoreResource(Resource):
    def get(self, store_id):
        store = Store.query.get_or_404(store_id)
        return jsonify(store_schema.dump(store))

    def put(self, store_id):
        store = Store.query.get_or_404(store_id)
        parser = reqparse.RequestParser()
        parser.add_argument('store_name', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('status', type=str)
        args = parser.parse_args()

        store.store_name = args['store_name'] or store.store_name
        store.city = args['city'] or store.city
        store.status = args['status'] or store.status

        db.session.commit()
        return jsonify(store_schema.dump(store))

    def delete(self, store_id):
        store = Store.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return '', 204

class StoresResource(Resource):
    def get(self):
        stores = Store.query.all()
        return jsonify(stores_schema.dump(stores))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('store_name', type=str, required=True)
        parser.add_argument('city', type=str, required=True)
        parser.add_argument('status', type=str, required=True)
        args = parser.parse_args()

        new_store = Store(name=args['store_name'], location=args['city'], products=args['status'])
        db.session.add(new_store)
        db.session.commit()
        return jsonify(store_schema.dump(new_store)), 201
