# Bold Store - Modern E-Commerce Application

A stunning, modern e-commerce web application built with Django, featuring a bold dark theme with neon green accents, glassmorphism design, and smooth animations.

## 📋 Project Structure

```
eccormmerce/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── media/                   # User uploads (product images)
├── staticfiles/             # Collected static files
│
├── eccormmerce/             # Project settings
│   ├── __init__.py
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
└── store/                   # Main application
    ├── migrations/          # Database migrations
    ├── templates/store/     # HTML templates
    │   ├── base.html        # Base template with navigation
    │   ├── home.html        # Homepage with hero section
    │   ├── products.html    # Product listing page
    │   ├── cart.html        # Shopping cart page
    │   ├── checkout.html    # Checkout form
    │   └── confirmation.html # Order confirmation
    │
    ├── static/store/        # CSS, JS, images
    │   ├── css/
    │   │   └── style.css    # Modern styling with animations
    │   └── js/
    │       └── app.js       # Interactive functionality
    │
    ├── admin.py             # Django admin configuration
    ├── apps.py              # App configuration
    ├── forms.py             # Django forms (CheckoutForm)
    ├── models.py            # Database models (Product, Order, OrderItem)
    ├── tests.py
    ├── urls.py              # App URL routing
    └── views.py             # View logic
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- pip (Python package manager)

### 2. Installation

```bash
# Navigate to your project directory
cd eccormmerce

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Django (if not already installed)
pip install django pillow
```

### 3. Database Setup

```bash
# Apply migrations
python manage.py migrate

# Create a superuser for the admin panel
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### 4. Add Sample Products

```bash
python manage.py shell
```

Then run this code in the Django shell:

```python
from store.models import Product

# Create sample products
products = [
    Product(
        name="Iron Pulse",
        price=49.99,
        category="electronics",
        description="Premium wireless headphones with noise cancellation"
    ),
    Product(
        name="Noir Velocity",
        price=69.99,
        category="electronics",
        description="Sleek mechanical keyboard with RGB lighting"
    ),
    Product(
        name="Urban Shield",
        price=89.99,
        category="clothing",
        description="Minimalist backpack for modern professionals"
    ),
    Product(
        name="Nova Watch",
        price=199.99,
        category="electronics",
        description="Smart watch with advanced health tracking"
    ),
    Product(
        name="Chrono Flex",
        price=45.99,
        category="clothing",
        description="Comfortable athletic wear for daily use"
    ),
    Product(
        name="Prism Gear",
        price=129.99,
        category="electronics",
        description="Professional camera with 4K video recording"
    ),
]

for product in products:
    product.save()

print("Products created successfully!")
exit()
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📖 Pages Overview

### 🏠 Homepage (`/`)
- Bold hero section with animated gradient background
- Featured products section with magazine-style layout
- Sticky navigation bar with cart counter
- Call-to-action section

### 🛍️ Products Page (`/products/`)
- Display all products in a responsive grid
- Real-time search functionality (Ctrl+K shortcut)
- Category filter buttons
- Hover effects on product cards
- Add to cart buttons

### 🛒 Cart Page (`/cart/`)
- List all items with quantity and price
- Remove items functionality
- Cart summary with total price
- Proceed to checkout button
- Empty cart state with encouragement to shop

### 📋 Checkout Page (`/checkout/`)
- Beautiful form with glassmorphic design
- Fields: Full Name, Email, Address, City, Phone
- Django form validation
- Order summary display
- Security information

### ✅ Confirmation Page (`/order-confirmed/`)
- Order confirmation message
- Order number and date
- Complete order details
- Order items list
- Next steps information

## 🎨 Design Features

### Color Palette
- **Primary Dark**: `#0f172a` (Deep navy background)
- **Secondary Dark**: `#1e293b` (Card backgrounds)
- **Accent Green**: `#22c55e` (Neon green for highlights)
- **Text Primary**: `#f8fafc` (White text)
- **Text Secondary**: `#cbd5e1` (Gray text)

### Typography
- **Font**: Space Grotesk, Syne (from Google Fonts)
- **Font Weights**: 400-800 for varied hierarchy

### Effects
- ✨ Glassmorphism (frosted glass effect)
- 🎯 Smooth animations and transitions
- 🔆 Glow effects on hover
- 📱 Fully responsive design
- ⚡ Micro-interactions on buttons and cards

## 🔧 Customization Guide

### Change Accent Color

Edit `store/static/store/css/style.css`:

```css
:root {
    --accent-green: #22c55e;      /* Change this hex code */
    --accent-green-glow: #16a34a;  /* Darker shade */
}
```

### Add Product Categories

Edit `store/models.py`:

```python
CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('home', 'Home & Garden'),      # Add new category
    ('sports', 'Sports & Outdoors'), # Add new category
]
```

Then create a new migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Modify Forms

Edit `store/forms.py` to add/remove form fields:

```python
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'city', 'phone', 'country']  # Add 'country'
```

## 🖼️ Adding Product Images

1. Create a `media/products/` directory in your project root
2. Upload product images to the admin panel:
   - Go to `http://127.0.0.1:8000/admin/`
   - Click on "Products"
   - Click "Add Product"
   - Fill in the form and upload an image
3. Images will be served from `/media/products/`

## 📱 Responsive Design

The application is fully responsive:
- **Desktop**: Full featured layout with all elements visible
- **Tablet**: Optimized grid and navigation
- **Mobile**: Stacked layout with touch-friendly buttons

Breakpoints:
- 768px: Medium screens (tablets)
- 480px: Small screens (mobile phones)

## 🛠️ Django Admin

Access the admin panel at `http://127.0.0.1:8000/admin/`

You can:
- Add/edit/delete products
- View and manage orders
- Track order items
- Monitor sales data

## 📊 Database Models

### Product
- `name`: CharField (product name)
- `price`: FloatField (product price)
- `category`: CharField (category selection)
- `image`: ImageField (product image)
- `description`: TextField (product description)

### Order
- `full_name`: CharField (customer name)
- `email`: EmailField (customer email)
- `address`: TextField (delivery address)
- `city`: CharField (delivery city)
- `phone`: CharField (customer phone)
- `created_at`: DateTimeField (auto-generated timestamp)

### OrderItem
- `product`: ForeignKey (reference to Product)
- `order`: ForeignKey (reference to Order)
- `quantity`: IntegerField (item quantity)

## 🔐 Session Management

Cart data is stored in Django sessions:
- Items are stored as a dictionary: `{product_id: quantity}`
- Sessions persist across page refreshes
- Cart is cleared after order completion
- No user authentication required

## 📦 Production Deployment

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Update Settings

In `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### Security

- Change the SECRET_KEY in production
- Use environment variables for sensitive data
- Set HTTPS
- Configure CORS if needed

## 🐛 Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --clear --noinput
```

### Database issues
```bash
python manage.py migrate --run-syncdb
```

### Port already in use
```bash
python manage.py runserver 8001  # Use different port
```

## 📝 Features Implemented

✅ Product catalog with categories
✅ Real-time search functionality
✅ Shopping cart (session-based)
✅ Checkout with form validation
✅ Order confirmation
✅ Modern, dark UI with neon accent
✅ Glassmorphism design
✅ Smooth animations
✅ Fully responsive design
✅ Mobile-optimized
✅ Admin panel for product management
✅ Static CSS and JS files
✅ Product images support

## 🎯 Future Enhancements

- User authentication & wishlist
- Payment gateway integration
- Order tracking system
- Product reviews & ratings
- Email notifications
- Advanced filtering & sorting
- Product recommendations
- Inventory management
- Analytics dashboard

## 📄 License

This project is open-source and available under the MIT License.

## 🤝 Support

For issues or questions, please refer to the Django documentation:
- Django Docs: https://docs.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/stable/topics/db/models/
- Django Forms: https://docs.djangoproject.com/en/stable/topics/forms/

---

**Happy shopping! 🛍️**