from app import app, db
from .models import User, Profile, Product, Orders, Store
from datetime import datetime


with app.app_context():
    users = [
        {'username': 'adolf', 'email': 'here@gmail.com', 'password': 'password', 'city': 'New York'},
        {'username': 'nyerere', 'email': 'there@gmail.com', 'password': 'password', 'city': 'Los Angeles'},
        
    ]

    for user in users:
        new_user = User(**user)
        db.session.add(new_user)

    db.session.commit()
    print("👤 Users seeded!")


    profiles = [
        {'firstname': 'Hitler', 'lastname': 'Adolf', 'contact_info': '1234567890', 'city': 'Kiambu'},
        {'firstname': 'Tenant', 'lastname': 'Earth', 'contact_info': '9876543210', 'city': 'Juja'},
    ]

    for profile_data in profiles:
        user = User.query.filter_by(username=profile_data['username']).first()
        profile = Profile(**profile_data, user=user)
        db.session.add(profile)

    db.session.commit()
    print("👤 Profiles seeded!")
    
        
    
    products = [
        {'product_name': 'Samsung TV', 'Price': '67890'},
        {'product_name': 'LG TV', 'Price': '76890'},
    ]

    for product_data in products:
        product = Product(**product_data)
        db.session.add(product)

    db.session.commit()
    print("👤 Products seeded!")
    
    
    
    
    orders = [
        {'date': '2024-01-23', 'quantity': '4'},
        {'date': '2024-03-22', 'quantity': '2'},
    ]

    for order_data in orders:
        order = Orders(**order_data)
        db.session.add(order)

    db.session.commit()
    print("👤 Orders seeded!")

    stores = [
        {'store_name': 'naivas', 'city': 'Nairobi', 'status': 'Available'},
        {'store_name': 'naivas', 'city': 'Nairobi', 'status': 'Available'},
    ]

    for store_data in stores:
        store = Store(**store_data)
        db.session.add(store)

    db.session.commit()
    print("👤 Stores seeded!")

    print(" Database seeding completed!")



