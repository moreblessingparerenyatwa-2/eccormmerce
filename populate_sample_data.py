#!/usr/bin/env python
"""
Sample data initialization script for Bold Store
Run with: python populate_sample_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eccormmerce.settings')
django.setup()

from store.models import Product

def create_sample_products():
    """Create sample products for testing"""
    
    products_data = [
        {
            'name': 'Iron Pulse',
            'price': 49.99,
            'category': 'electronics',
            'description': 'Premium wireless headphones with active noise cancellation, 30-hour battery life, and premium sound quality.'
        },
        {
            'name': 'Noir Velocity',
            'price': 69.99,
            'category': 'electronics',
            'description': 'Sleek mechanical keyboard with customizable RGB lighting and ultra-responsive switches.'
        },
        {
            'name': 'Urban Shield',
            'price': 89.99,
            'category': 'clothing',
            'description': 'Minimalist backpack for modern professionals with laptop compartment and water-resistant material.'
        },
        {
            'name': 'Nova Watch',
            'price': 199.99,
            'category': 'electronics',
            'description': 'Smart watch with advanced health tracking, ECG monitoring, and 7-day battery life.'
        },
        {
            'name': 'Chrono Flex',
            'price': 45.99,
            'category': 'clothing',
            'description': 'Comfortable athletic wear for daily use with breathable fabric and ergonomic design.'
        },
        {
            'name': 'Prism Gear',
            'price': 129.99,
            'category': 'electronics',
            'description': 'Professional camera with 4K video recording, 20MP sensor, and advanced autofocus system.'
        },
        {
            'name': 'Vortex Max',
            'price': 159.99,
            'category': 'electronics',
            'description': 'High-performance gaming mouse with adjustable DPI and customizable buttons.'
        },
        {
            'name': 'Zenith Case',
            'price': 79.99,
            'category': 'clothing',
            'description': 'Premium laptop case with shock absorption and elegant minimalist design.'
        },
        {
            'name': 'Quantum Stream',
            'price': 249.99,
            'category': 'electronics',
            'description': 'Ultra-high-speed USB 3.1 external SSD with 2TB storage capacity.'
        },
        {
            'name': 'Apex Spirit',
            'price': 34.99,
            'category': 'clothing',
            'description': 'Lightweight hoodie perfect for casual wear and layering.'
        },
    ]
    
    created_count = 0
    skipped_count = 0
    
    print("🚀 Creating sample products...")
    print("-" * 50)
    
    for product_data in products_data:
        # Check if product already exists
        if Product.objects.filter(name=product_data['name']).exists():
            print(f"⏭️  Skipped: {product_data['name']} (already exists)")
            skipped_count += 1
        else:
            Product.objects.create(**product_data)
            print(f"✅ Created: {product_data['name']}")
            created_count += 1
    
    print("-" * 50)
    print(f"\n📊 Summary:")
    print(f"   Created: {created_count} products")
    print(f"   Skipped: {skipped_count} products")
    print(f"   Total: {Product.objects.count()} products in database")
    print("\n✨ Sample data setup complete!")

if __name__ == '__main__':
    try:
        create_sample_products()
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)