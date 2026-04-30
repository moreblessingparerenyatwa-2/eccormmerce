#!/bin/bash

echo "================================"
echo "Bold Store - Setup Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "Step 1: Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error creating virtual environment"
    exit 1
fi

echo "Step 2: Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error activating virtual environment"
    exit 1
fi

echo "Step 3: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error installing dependencies"
    exit 1
fi

echo "Step 4: Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error running migrations"
    exit 1
fi

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "Next steps:"
echo "1. Create a superuser:"
echo "   python manage.py createsuperuser"
echo ""
echo "2. Add sample products (run these in Django shell):"
echo "   python manage.py shell"
echo ""
echo "3. Run the development server:"
echo "   python manage.py runserver"
echo ""
echo "4. Open your browser to:"
echo "   http://127.0.0.1:8000/"
echo ""
echo "5. Access admin panel:"
echo "   http://127.0.0.1:8000/admin/"
echo ""