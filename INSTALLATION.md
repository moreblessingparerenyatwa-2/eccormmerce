# Bold Store - Complete Installation & Setup Guide

## 🎯 Complete Setup Instructions

### Step 1: Extract and Navigate to Project

```bash
# Navigate to your project directory
cd "c:\Users\UncommonStudent\Desktop\django eccormmerce"
```

### Step 2: Run Automated Setup (Windows)

**Option A: Automatic Setup (Recommended)**

```bash
# Double-click setup.bat (Windows)
setup.bat
```

**Option B: Manual Setup**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate
```

### Step 3: Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 4: Add Sample Products

```bash
python populate_sample_data.py
```

Or manually in Django shell:

```bash
python manage.py shell
```

Then paste this code:

```python
from store.models import Product

products = [
    Product(name="Iron Pulse", price=49.99, category="electronics", description="Premium wireless headphones"),
    Product(name="Noir Velocity", price=69.99, category="electronics", description="Mechanical keyboard with RGB"),
    Product(name="Urban Shield", price=89.99, category="clothing", description="Minimalist backpack"),
    Product(name="Nova Watch", price=199.99, category="electronics", description="Smart watch with health tracking"),
]

for p in products:
    p.save()

exit()
```

### Step 5: Start Development Server

```bash
python manage.py runserver
```

### Step 6: Access the Application

- **Frontend**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📁 File Structure & Locations

### Backend Files

| File | Location | Purpose |
|------|----------|---------|
| `models.py` | `store/models.py` | Database models (Product, Order, OrderItem) |
| `views.py` | `store/views.py` | View logic and request handlers |
| `urls.py` | `store/urls.py` | URL routing for the store app |
| `forms.py` | `store/forms.py` | Django form for checkout |
| `admin.py` | `store/admin.py` | Django admin configuration |
| `settings.py` | `eccormmerce/settings.py` | Django project settings |

### Frontend Files

| File | Location | Purpose |
|------|----------|---------|
| `base.html` | `store/templates/store/base.html` | Base template with navigation |
| `home.html` | `store/templates/store/home.html` | Homepage with hero & featured products |
| `products.html` | `store/templates/store/products.html` | Product listing page |
| `cart.html` | `store/templates/store/cart.html` | Shopping cart |
| `checkout.html` | `store/templates/store/checkout.html` | Checkout form |
| `confirmation.html` | `store/templates/store/confirmation.html` | Order confirmation |

### Static Files

| File | Location | Purpose |
|------|----------|---------|
| `style.css` | `store/static/store/css/style.css` | Main stylesheet with modern design |
| `app.js` | `store/static/store/js/app.js` | JavaScript for interactivity |

---

## 🔧 Configuration Changes Made

### 1. **settings.py Updates**

```python
# Added media file configuration
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 2. **urls.py Updates**

```python
# Added support for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. **forms.py Enhancement**

```python
# Added CSS classes and placeholders to form widgets
widgets = {
    'full_name': forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Full Name'
    }),
    # ... other fields
}
```

### 4. **views.py Enhancement**

```python
# Enhanced all views with:
# - Cart count in context
# - Better error handling
# - Proper session management
# - Order creation and confirmation logic
```

---

## 🎨 Design System

### Colors
```css
Primary Dark: #0f172a
Secondary Dark: #1e293b
Accent Green: #22c55e
Text Primary: #f8fafc
Text Secondary: #cbd5e1
```

### Components
- **Cards**: Glassmorphic with backdrop blur
- **Buttons**: Pill-shaped with glow effects
- **Forms**: Styled inputs with focus states
- **Navigation**: Sticky with smooth animations

### Responsive Breakpoints
- Desktop: 1024px+
- Tablet: 768px - 1023px
- Mobile: Below 768px

---

## 🚀 Running the Application

### Development Mode

```bash
# Activate virtual environment (if not already)
venv\Scripts\activate

# Run server
python manage.py runserver

# Server running at: http://127.0.0.1:8000/
```

### Access Points

1. **Homepage**: `http://127.0.0.1:8000/`
2. **Products**: `http://127.0.0.1:8000/products/`
3. **Cart**: `http://127.0.0.1:8000/cart/`
4. **Checkout**: `http://127.0.0.1:8000/checkout/`
5. **Admin**: `http://127.0.0.1:8000/admin/`

---

## 📊 Database Management

### View Database Content

```bash
python manage.py dbshell
```

### Reset Database (CAUTION!)

```bash
# Delete db.sqlite3
# Then run migrations again
python manage.py migrate
```

### Create Backups

```bash
# Copy db.sqlite3 to a safe location
copy db.sqlite3 db.sqlite3.backup
```

---

## 🆘 Common Issues & Solutions

### Issue: "Static files not loading"
**Solution:**
```bash
python manage.py collectstatic --clear --noinput
python manage.py runserver
```

### Issue: "ModuleNotFoundError: No module named 'PIL'"
**Solution:**
```bash
pip install Pillow
```

### Issue: "Port 8000 already in use"
**Solution:**
```bash
python manage.py runserver 8001
```

### Issue: "Database locked"
**Solution:**
```bash
# Delete db.sqlite3 and recreate
python manage.py migrate
```

---

## 📝 Development Checklist

Before deploying to production, ensure:

- [ ] All products have images
- [ ] Admin account created
- [ ] Sample products added
- [ ] Forms validated and working
- [ ] Cart functionality tested
- [ ] Checkout process tested
- [ ] Email confirmation configured (optional)
- [ ] Static files collected
- [ ] DEBUG set to False
- [ ] SECRET_KEY changed
- [ ] ALLOWED_HOSTS configured

---

## 🔐 Security Notes

1. **Never commit `.env` file**
2. **Change SECRET_KEY before production**
3. **Use HTTPS in production**
4. **Set DEBUG = False in production**
5. **Keep Django and dependencies updated**
6. **Validate all user inputs**

---

## 📚 Useful Commands

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Enter Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Change password
python manage.py changepassword <username>

# Clear cache
python manage.py clear_cache
```

---

## 🎓 Learning Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Django Models**: https://docs.djangoproject.com/en/stable/topics/db/models/
- **Django Forms**: https://docs.djangoproject.com/en/stable/topics/forms/
- **Django Templates**: https://docs.djangoproject.com/en/stable/topics/templates/
- **CSS Grid**: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout
- **Flexbox**: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout

---

## 🎉 You're All Set!

Your Bold Store application is now ready to use. Start by:

1. Running the development server
2. Accessing the admin panel
3. Adding some products
4. Testing the shopping experience

Happy coding! 🚀