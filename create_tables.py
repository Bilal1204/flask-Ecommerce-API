import sqlite3

db_location = "data.db"

connection = sqlite3.connect(db_location)
cursor = connection.cursor()

create_product_table = """
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image_url TEXT
)
"""

create_cart_item_table = """
CREATE TABLE IF NOT EXISTS CartItem (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Product(id)
)
"""

cursor.execute(create_product_table)
cursor.execute(create_cart_item_table)


connection.commit()
connection.close()