# 🚗 CarNova

**CarNova** is a modern Vehicle Inventory & Dealership Management System built using **Django**, **Django REST Framework**, **JWT Authentication**, **SQLite**, **Tailwind CSS**, and **JavaScript**.

The application enables dealerships to manage inventory, maintain vehicle records, monitor stock, and simulate vehicle purchases through a clean, responsive dashboard.

---

## Features

### Authentication
- JWT Authentication
- User Registration
- Secure Login
- Protected API Endpoints

### Vehicle Management
- Add Vehicles
- Edit Vehicles
- View Vehicle Details
- Delete Vehicles
- Upload Vehicle Images

### Inventory Management
- Live Inventory Dashboard
- Stock Quantity Tracking
- Low Stock Detection
- Out-of-Stock Status

### Vehicle Purchase
- Purchase Simulation
- Automatic Inventory Reduction
- Live Status Update
- Dynamic Stock Badges

### Dashboard
- Vehicle Overview
- Inventory Statistics
- Revenue Summary
- Low Stock Monitoring

### Search
- Search by Make
- Search by Model
- Category Filtering

### UI
- Responsive Design
- Tailwind CSS
- Modern Dashboard
- Mobile Friendly
- Clean User Experience

---

# Technology Stack

## Backend

- Python
- Django
- Django REST Framework
- Simple JWT

## Frontend

- HTML5
- Tailwind CSS
- JavaScript
- Fetch API

## Database

- SQLite

## Version Control

- Git
- GitHub

## Deployment

- Render

---

# Project Structure

```
CarNova/

accounts/
backend/
frontend/
vehicles/

templates/

static/
    css/
    js/
    images/

media/

manage.py
requirements.txt
README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Tanay6803/CarNova.git
```

Move inside project

```bash
cd CarNova
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Start Server

```bash
python manage.py runserver
```

---

# Screens

- Home
- Login
- Register
- Dashboard
- Add Vehicle
- Edit Vehicle
- Vehicle Details

---

# API Endpoints

Authentication

```
POST /api/auth/register/

POST /api/auth/login/
```

Vehicles

```
GET /api/vehicles/

POST /api/vehicles/

PUT /api/vehicles/<id>/

DELETE /api/vehicles/<id>/
```

Purchase

```
POST /api/vehicles/<id>/purchase/
```

---

# Future Enhancements

- Customer Management
- Sales Analytics
- PDF Invoice Generation
- Excel Reports
- Email Notifications
- Role Based Access
- Charts & Graphs
- PostgreSQL Support

---

# Author

**Tanay**

Master of Computer Applications (MCA)

---

# License

This project is developed for educational purposes as an MCA Major Project.