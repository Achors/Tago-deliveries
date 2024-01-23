from app import app, db
from app.models import User, Profile, Product, Orders, Store
from datetime import datetime


with app.app_context():
    users = [
        {'username': 'adolf', 'email': 'here@gmail.com', 'password': 'password', 'city': 'New York'},
        {'username': 'nyerere', 'email': 'there@gmail.com', 'password': 'password', 'city': 'Los Angeles'},
        
    ]

    for user in users:
        user = User(**users)
        db.session.add(user)

    db.session.commit()
    print("👤 Users seeded!")


    profiles = [
        {'firstname': 'Hitler', 'lastname': 'Adolf', 'contact_info': '1234567890', 'city': 'Kiambu'},
        {'firstname': 'Tenant', 'lastname': 'Earth', 'contact_info': '9876543210', 'city': 'Juja'},
    
    ]

    for profile in profiles:
        profile = Profile(**profile, user=User.query.filter_by(username=profiles['username']).first())
        db.session.add(profile)

    db.session.commit()
    print("👤 Profiles seeded!")
    
        
    
    products = [
        {'product_name': 'Samsung TV', 'Price': '67890'},
        {'product_name': 'LG TV', 'Price': '76890'},
        
    
    ]

    for product in products:
        product = Product(**products)
        db.session.add(product)

    db.session.commit()
    print("👤 Products seeded!")
    
    
    
    
    orders = [
        {'date': '2024-01-23', 'quantity': '4'},
        {'date': '2024-03-22', 'quantity': '2'},
        
    ]

    for order in orders:
        order = Orders(**orders)
        db.session.add(order)

    db.session.commit()
    print("👤 orders seeded!")

    stores = [
        {'store_name': 'naivas', 'city': 'Nairobi', 'status': 'Available'},
        {'store_name': 'naivas', 'city': 'Nairobi', 'status': 'Available'},
    
    ]

    for store in stores:
        store = Store(**stores)
        db.session.add(store)

    db.session.commit()
    print("👤 Stores seeded!")

    print(" Database seeding completed!")



