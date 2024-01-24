from flask_restful import Resource, reqparse
from models import db, Order
from schema import OrderSchema
from flask import jsonify

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class Order(Resource):
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return jsonify(order_schema.dump(order))

    def put(self, order_id):
        order = Order.query.get_or_404(order_id)
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str)
        parser.add_argument('quantity', type=int)
        parser.add_argument('total_price', type=float)
        args = parser.parse_args()


        order.product_name = args['product_name'] or order.product_name
        order.quantity = args['quantity'] or order.quantity
        order.total_price = args['total_price'] or order.total_price

        db.session.commit()
        return jsonify(order_schema.dump(order))

    def delete(self, order_id):
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return '', 204

class Orders(Resource):
    def get(self):
        orders = Order.query.all()
        return jsonify(orders_schema.dump(orders))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('quantity', type=int, required=True)
        parser.add_argument('total_price', type=float, required=True)
        args = parser.parse_args()

        new_order = Order(
            product_name=args['product_name'],
            quantity=args['quantity'],
            total_price=args['total_price']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
