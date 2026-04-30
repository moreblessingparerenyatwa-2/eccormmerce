# Bold Store - Quick Reference Guide

## 🚀 Quick Start (60 seconds)

```bash
# 1. Navigate to project
cd "c:\Users\UncommonStudent\Desktop\django eccormmerce"

# 2. Run setup
setup.bat

# 3. Create admin user
python manage.py createsuperuser

# 4. Add sample products
python populate_sample_data.py

# 5. Start server
python manage.py runserver

# 6. Open browser
# Frontend: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

## 📁 File Location Reference

### Core Backend
```
store/
├── models.py          → Database models
├── views.py           → Request handlers
├── urls.py            → URL routing
├── forms.py           → Django forms
└── admin.py           → Admin configuration
```

### Templates
```
templates/store/
├── base.html          → Navigation & layout
├── home.html          → Homepage with hero
├── products.html      → Product listing
├── cart.html          → Shopping cart
├── checkout.html      → Checkout form
└── confirmation.html  → Order confirmation
```

### Static Assets
```
static/store/
├── css/
│   └── style.css      → Main stylesheet (1000+ lines)
└── js/
    └── app.js         → JavaScript (400+ lines)
```

### Configuration
```
root/
├── eccormmerce/
│   ├── settings.py    → Django settings
│   ├── urls.py        → Main URL config
│   └── wsgi.py
│
├── README.md          → Full documentation
├── INSTALLATION.md    → Setup guide
├── IMPLEMENTATION_SUMMARY.md → What was done
├── requirements.txt   → Python dependencies
└── populate_sample_data.py → Sample data script
```

---

## 🎯 Main Routes

| Route | Purpose | Method |
|-------|---------|--------|
| `/` | Homepage | GET |
| `/products/` | Product listing | GET |
| `/products/?category=electronics` | Filter by category | GET |
| `/cart/` | Shopping cart | GET |
| `/add/<id>/` | Add to cart | GET |
| `/remove/<id>/` | Remove from cart | GET |
| `/checkout/` | Checkout form | GET/POST |
| `/order-confirmed/` | Order confirmation | GET |
| `/admin/` | Django admin | GET |

---

## 🎨 Customization Quick Guide

### Change Accent Color
**File**: `store/static/store/css/style.css` (Line 8-9)
```css
--accent-green: #22c55e;      /* Your color here */
--accent-green-glow: #16a34a; /* Darker shade */
```

### Change Logo
**File**: `store/templates/store/base.html` (Line 26)
```html
<span>⚡</span>  <!-- Change emoji or add logo image -->
```

### Add New Category
**File**: `store/models.py`
```python
CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('new_category', 'New Category'),  # Add here
]
```

### Modify Product Fields
**File**: `store/models.py`
```python
class Product(models.Model):
    # ... existing fields ...
    new_field = models.CharField(max_length=100)  # Add here
```

---

## 🐛 Troubleshooting Quick Fix

| Problem | Solution |
|---------|----------|
| Static files not loading | `python manage.py collectstatic --clear --noinput` |
| Module not found | `pip install -r requirements.txt` |
| Port in use | `python manage.py runserver 8001` |
| Database error | Delete `db.sqlite3`, then run `python manage.py migrate` |
| Image not showing | Ensure image file in `media/products/` and product.image is set |
| 404 on admin | Make sure you're at `/admin/` (with trailing slash) |

---

## 📊 Database Commands

```bash
# Show all tables
python manage.py dbshell

# Create backup
copy db.sqlite3 db.sqlite3.backup

# Reset database (CAREFUL!)
del db.sqlite3
python manage.py migrate

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View all migrations
python manage.py showmigrations
```

---

## 👨‍💼 Admin Panel Guide

### Add Product
1. Go to `/admin/`
2. Click "Products"
3. Click "Add Product"
4. Fill in: Name, Price, Category, Image, Description
5. Click "Save"

### View Orders
1. Go to `/admin/`
2. Click "Orders"
3. See all customer orders
4. Click order to view details

### Create User
1. Go to `/admin/`
2. Click "Users"
3. Click "Add User"
4. Set username and password
5. Click "Save"

---

## 💡 Development Tips

### Activate Virtual Environment Every Time
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### Django Shell for Testing
```bash
python manage.py shell
>>> from store.models import Product
>>> Product.objects.all()
>>> exit()
```

### View Server Logs
Watch the terminal where `python manage.py runserver` is running for:
- Request logs
- Error messages
- SQL queries (in DEBUG mode)

### Test Search Feature
- Press `Ctrl+K` in products page to focus search
- Type to filter products in real-time

---

## 📱 Testing Responsive Design

### Browser DevTools
1. Open DevTools (F12)
2. Click device toggle icon
3. Select device (iPhone, iPad, etc.)
4. Test functionality on each screen size

### Responsive Sizes to Test
- Mobile: 360px, 414px
- Tablet: 768px, 1024px
- Desktop: 1366px+

---

## 🔒 Before Going Live

- [ ] Change `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to random string
- [ ] Set `ALLOWED_HOSTS = ['yourdomain.com']`
- [ ] Set up HTTPS
- [ ] Use environment variables for secrets
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Test all forms
- [ ] Test payment flow
- [ ] Set up email notifications (optional)
- [ ] Create database backup

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| `README.md` | Full project documentation |
| `INSTALLATION.md` | Detailed setup guide |
| `IMPLEMENTATION_SUMMARY.md` | What was built |
| `QUICK_REFERENCE.md` | This file |

---

## 🆘 Getting Help

### For Django Help
- Django Docs: https://docs.djangoproject.com/
- Stack Overflow: Tag with `django`
- Django Forum: https://forum.djangoproject.com/

### For Design Help
- CSS Tricks: https://css-tricks.com/
- MDN Web Docs: https://developer.mozilla.org/
- Google Fonts: https://fonts.google.com/

---

## 🎓 Learning Path

1. **Understand Models**: Read `store/models.py`
2. **Learn Views**: Read `store/views.py`
3. **Study Templates**: Read templates in `templates/store/`
4. **Explore Styling**: Read `store/static/store/css/style.css`
5. **Review JavaScript**: Read `store/static/store/js/app.js`

---

## ✅ Success Checklist

- [ ] Project extracted and navigated to
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Database migrated
- [ ] Admin user created
- [ ] Sample products added
- [ ] Server running without errors
- [ ] Homepage loads and looks good
- [ ] Can add items to cart
- [ ] Can navigate between pages
- [ ] Admin panel accessible
- [ ] Mobile view responsive

---

## 🎉 You're Ready!

Your Bold Store is now fully set up and ready to use. 

**Next Steps:**
1. Add more products in admin panel
2. Customize the design to match your brand
3. Test all functionality
4. Consider adding features like:
   - User accounts
   - Wishlist
   - Reviews
   - Email notifications

Enjoy your modern e-commerce platform! 🚀

---

## Version Info
- **Django**: 6.0.4
- **Python**: 3.8+
- **Database**: SQLite3
- **Last Updated**: 2024