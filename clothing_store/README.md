# Clothing Store

A simple e-commerce clothing store built with Flask, featuring a responsive front-end, cart functionality, and an admin panel for product management.

## Features

- Home page with featured products
- Product listing with search and filters
- Product detail pages with add to cart
- Shopping cart with quantity management
- Checkout form (no real payment processing)
- Admin panel for CRUD operations on products (password protected)
- Responsive design with accessibility considerations (WCAG AA)
- MySQL database for data storage

## Installation

1. Ensure you have Python 3.10+ and MySQL installed.

2. Create a MySQL database named `clothing_store` (or update `.env` accordingly).

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Update `.env` with your MySQL credentials:
   ```
   DB_HOST=localhost
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_NAME=clothing_store
   ```

7. Seed the database with sample products:
   ```
   python data/seed.py
   ```

## Running the Application

1. Run the Flask app:
   ```
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`

## Admin Access

- To access the admin panel, go to `/login` and use the password from `.env` (default: admin123)
- Change the `ADMIN_PASSWORD` in `.env` for security.

## Project Structure

```
clothing_store/
├── app.py                 # Main Flask application
├── models.py              # Database models and functions
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── data/
│   └── seed.py            # Database seeding script
├── static/
│   └── css/
│       └── style.css      # Custom CSS styles
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── products.html      # Product listing
│   ├── product_detail.html # Product detail
│   ├── cart.html          # Shopping cart
│   ├── checkout.html      # Checkout form
│   ├── admin.html         # Admin panel
│   └── login.html         # Admin login
└── README.md
```

## Technologies Used

- Python 3.10+
- Flask
- MySQL
- Jinja2 templates
- Custom CSS (responsive and accessible)

## Accessibility

The site aims for WCAG AA compliance with:
- Semantic HTML
- Proper contrast ratios
- Keyboard navigation
- ARIA attributes where needed
- Alt text for images

## Sample Data

The seed script adds 8 sample products across categories like Tops, Bottoms, Outerwear, etc.
