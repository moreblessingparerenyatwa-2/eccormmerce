#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eccormmerce.settings')
django.setup()

from store.models import Product

# Get all products
products = Product.objects.all()
images = [
    'products/pexels-b-o-phuc-34482444-12355945.jpg',
    'products/pexels-ethan-harvey-28794306-6860977.jpg',
    'products/pexels-nguy-n-ti-n-th-nh-2150376175-33409535.jpg',
    'products/pexels-puruxraj-33496220.jpg',
    'products/pexels-soc-nang-d-ng-2150345854-32339427.jpg',
    'products/pexels-soc-nang-d-ng-2150345854-34602506.jpg',
]

print(f"Found {len(products)} products and {len(images)} images")
print("\nUpdating products with images...\n")

# Assign images to products
for i, product in enumerate(products):
    if i < len(images):
        product.image = images[i]
        product.save()
        print(f"✓ {product.name} -> {images[i]}")
    else:
        break

print("\n✅ Done! All products updated with images.")
print("Refresh your browser to see the changes: http://127.0.0.1:8000/products/")
