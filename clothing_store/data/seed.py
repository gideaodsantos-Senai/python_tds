from models import init_db, add_product

def seed_db():
    init_db()
    products = [
        {
            'name': 'Casual T-Shirt',
            'description': 'Comfortable cotton t-shirt for everyday wear.',
            'price': 25.99,
            'category': 'Tops',
            'image_url': '/static/images/tshirt.svg',
            'sizes': 'S,M,L,XL'
        },
        {
            'name': 'Denim Jeans',
            'description': 'Classic blue denim jeans with a slim fit.',
            'price': 79.99,
            'category': 'Bottoms',
            'image_url': '/static/images/jeans.svg',
            'sizes': '28,30,32,34'
        },
        {
            'name': 'Leather Jacket',
            'description': 'Stylish black leather jacket for a bold look.',
            'price': 149.99,
            'category': 'Outerwear',
            'image_url': '/static/images/jacket.svg',
            'sizes': 'S,M,L,XL'
        },
        {
            'name': 'Summer Dress',
            'description': 'Light and airy summer dress in floral print.',
            'price': 49.99,
            'category': 'Dresses',
            'image_url': '/static/images/dress.svg',
            'sizes': 'XS,S,M,L'
        },
        {
            'name': 'Sneakers',
            'description': 'Comfortable white sneakers for casual outings.',
            'price': 89.99,
            'category': 'Shoes',
            'image_url': '/static/images/sneakers.svg',
            'sizes': '7,8,9,10,11'
        },
        {
            'name': 'Wool Sweater',
            'description': 'Warm wool sweater for colder days.',
            'price': 69.99,
            'category': 'Tops',
            'image_url': '/static/images/sweater.svg',
            'sizes': 'S,M,L,XL'
        },
        {
            'name': 'Skirt',
            'description': 'Elegant midi skirt in black.',
            'price': 39.99,
            'category': 'Bottoms',
            'image_url': '/static/images/skirt.svg',
            'sizes': 'XS,S,M,L'
        },
        {
            'name': 'Hoodie',
            'description': 'Cozy hoodie with front pocket.',
            'price': 55.99,
            'category': 'Tops',
            'image_url': '/static/images/hoodie.svg',
            'sizes': 'S,M,L,XL'
        }
    ]
    for p in products:
        add_product(p['name'], p['description'], p['price'], p['category'], p['image_url'], p['sizes'])

if __name__ == '__main__':
    seed_db()
    print('Database seeded successfully.')
