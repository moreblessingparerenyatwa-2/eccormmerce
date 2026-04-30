@echo off
echo ================================
echo Bold Store - Setup Script
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo Step 1: Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error creating virtual environment
    pause
    exit /b 1
)

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error activating virtual environment
    pause
    exit /b 1
)

echo Step 3: Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)

echo Step 4: Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Error running migrations
    pause
    exit /b 1
)

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo Next steps:
echo 1. Create a superuser:
echo    python manage.py createsuperuser
echo.
echo 2. Add sample products (run these in Django shell):
echo    python manage.py shell
echo.
echo 3. Run the development server:
echo    python manage.py runserver
echo.
echo 4. Open your browser to:
echo    http://127.0.0.1:8000/
echo.
echo 5. Access admin panel:
echo    http://127.0.0.1:8000/admin/
echo.
pause