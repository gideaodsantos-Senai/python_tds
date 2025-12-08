from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from models import init_db, get_all_products, get_product_by_id, add_product, update_product, delete_product, search_products, get_categories
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

with app.app_context():
    init_db()

@app.route('/')
def index():
    products = get_all_products()
    featured = products[:3]  # First 3 as featured
    return render_template('index.html', featured=featured)

@app.route('/products')
def products():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    if query or category or min_price or max_price:
        products = search_products(query, category if category else None, min_price, max_price)
    else:
        products = get_all_products()
    categories = get_categories()
    return render_template('products.html', products=products, categories=categories, query=query, category=category, min_price=min_price, max_price=max_price)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        flash('Product not found.')
        return redirect(url_for('products'))
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    size = request.form.get('size')
    quantity = int(request.form.get('quantity', 1))
    if 'cart' not in session:
        session['cart'] = {}
    key = f"{product_id}_{size}"
    if key in session['cart']:
        session['cart'][key] += quantity
    else:
        session['cart'][key] = quantity
    session.modified = True
    flash('Product added to cart.')
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    if 'cart' in session:
        for key, qty in session['cart'].items():
            product_id, size = key.split('_', 1)
            product = get_product_by_id(int(product_id))
            if product:
                subtotal = product['price'] * qty
                total += subtotal
                cart_items.append({
                    'product': product,
                    'size': size,
                    'quantity': qty,
                    'subtotal': subtotal
                })
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/update_cart', methods=['POST'])
def update_cart():
    for key in list(session['cart'].keys()):
        new_qty = request.form.get(f'qty_{key}', type=int)
        if new_qty is None or new_qty <= 0:
            del session['cart'][key]
        else:
            session['cart'][key] = new_qty
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<key>')
def remove_from_cart(key):
    if 'cart' in session and key in session['cart']:
        del session['cart'][key]
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        # In real app, process payment here
        session.pop('cart', None)
        flash('Order placed successfully!')
        return redirect(url_for('index'))
    return render_template('checkout.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            add_product(
                request.form['name'],
                request.form['description'],
                float(request.form['price']),
                request.form['category'],
                request.form['image_url'],
                request.form['sizes']
            )
        elif action == 'edit':
            update_product(
                int(request.form['id']),
                request.form['name'],
                request.form['description'],
                float(request.form['price']),
                request.form['category'],
                request.form['image_url'],
                request.form['sizes']
            )
        elif action == 'delete':
            delete_product(int(request.form['id']))
        return redirect(url_for('admin'))
    products = get_all_products()
    return render_template('admin.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == os.getenv('ADMIN_PASSWORD'):
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
