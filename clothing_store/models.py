import sqlite3
import os

DB_PATH = 'data/db.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            image_url TEXT NOT NULL,
            sizes TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    return product

def add_product(name, description, price, category, image_url, sizes):
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, description, price, category, image_url, sizes) VALUES (?, ?, ?, ?, ?, ?)',
                 (name, description, price, category, image_url, sizes))
    conn.commit()
    conn.close()

def update_product(product_id, name, description, price, category, image_url, sizes):
    conn = get_db_connection()
    conn.execute('UPDATE products SET name = ?, description = ?, price = ?, category = ?, image_url = ?, sizes = ? WHERE id = ?',
                 (name, description, price, category, image_url, sizes, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

def search_products(query, category_filter=None, min_price=None, max_price=None):
    conn = get_db_connection()
    sql = 'SELECT * FROM products WHERE name LIKE ?'
    params = [f'%{query}%']
    if category_filter:
        sql += ' AND category = ?'
        params.append(category_filter)
    if min_price is not None:
        sql += ' AND price >= ?'
        params.append(min_price)
    if max_price is not None:
        sql += ' AND price <= ?'
        params.append(max_price)
    products = conn.execute(sql, params).fetchall()
    conn.close()
    return products

def get_categories():
    conn = get_db_connection()
    categories = conn.execute('SELECT DISTINCT category FROM products').fetchall()
    conn.close()
    return [row['category'] for row in categories]
