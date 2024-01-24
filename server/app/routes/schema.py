from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import User, Profile, Orders, Store, Product, Authorization


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile


class StoreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Store

class ProductSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = Product


class OrdersSchema(SQLAlchemyAutoSchema):
    profile = fields.Nested(ProfileSchema)
    Store = fields.Nested(StoreSchema)
    product = fields.Nested(ProductSchema)
    
    class Meta:
        model = Orders

class AuthorizationSchema(SQLAlchemyAutoSchema):
    user = fields.Nested(UserSchema)

    class Meta:
        model = Authorization