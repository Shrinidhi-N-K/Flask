from shop import create_app, db
from shop.models import Item

app = create_app()

with app.app_context():
    item1 = Item(name='Laptop', price=1200, barcode='123424542314', description='High-performance laptop')
    item2 = Item(name='Phone', price=1000, barcode='223412322314', description='Latest smartphone')
    item3 = Item(name='Keyboard', price=300, barcode='111122223333', description='Mechanical keyboard')
    item4 = Item(name='Monitor', price=600, barcode='444455556666', description='27-inch 4K monitor')
    item5 = Item(name='Headphones', price=250, barcode='777788889999', description='Noise-cancelling headphones')
    item6 = Item(name='Mouse', price=150, barcode='000011112222', description='Wireless gaming mouse')

    db.session.add_all([item1, item2, item3, item4, item5, item6])
    db.session.commit()

    print("✅ Items successfully added to the database.")