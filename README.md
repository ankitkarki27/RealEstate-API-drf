

# Real Estate Listings API

A full-featured **Real Estate Listing API** built with **Django REST Framework**, supporting **JWT authentication** for realtors and safe browsing for users.

---

## 📚 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Authentication (JWT)](#authentication-jwt)
- [API Endpoints](#api-endpoints)
- [Permissions](#permissions)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This project is a backend service for a real estate platform where **realtors** can:
- Create, update, and delete listings.
- Upload listing photos.
- Manage properties for sale, rent, or lease.

Meanwhile, **buyers and visitors** can:
- Browse active listings.
- Search listings by price, sales type, or property type.

✅ Authentication is secured via **JWT (JSON Web Tokens)**, ensuring that only authorized realtors can modify listings.

---

## 🚀 Features

- Realtor and user signup/login
- JWT-based authentication and authorization
- Create, view, update, delete (CRUD) listings
- Upload multiple property images
- Search and filter listings
- Permission restrictions (only realtor-owner can modify their listings)
- Django Admin integration

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** PostgreSQL | Easily swappable to MySQL
- **API Testing:** Postman


---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/real-estate-listing-api.git
cd real-estate-listing-api
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser

```bash
python manage.py createsuperuser
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

---
 
## Authentication (JWT)

This API uses **JWT Authentication** for login and token management.

### Token Endpoints:

| Method | URL | Purpose |
|:------:|:---:|:-------|
| POST | `/api/v1/token/` | Get Access and Refresh token |
| POST | `/api/v1/token/refresh/` | Refresh Access token |
| POST | `/api/v1/token/verify/` | Verify if token is valid |

### Login (Get Token)

```bash
POST http://localhost:8000/api/v1/token/
{
    "email": "realtor@example.com",
    "password": "yourpassword"
}
```

✅ Response:
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

Use the access token in headers for protected routes:

```http
Authorization: Bearer your_access_token
```

---

## API Endpoints

| Method | URL | Description |
|:------:|:---:|:-----------|
| GET | `/api/v1/listings/` | View all listings |
| POST | `/api/v1/listings/` | Create a new listing (Authenticated Realtor only) |
| GET | `/api/v1/listings/{id}/` | View single listing |
| PUT/PATCH | `/api/v1/listings/{id}/` | Update listing (Owner only) |
| DELETE | `/api/v1/listings/{id}/` | Delete listing (Owner only) |

---

## Permissions

| User | Actions Allowed |
|:----:|:---------------|
| **Unauthenticated User** | Can view listings only |
| **Authenticated Realtor** | Can create, update, and delete their own listings |

Custom permission class used: **IsRealtorOrReadOnly**

---

## Contributing

Contributions are welcome! Here's how you can help:
- Open issues
- Submit PRs (Pull Requests)
- Suggest new features
- Improve documentation

Please make sure your PRs are clean and tested.

---

##  License

This project is open-sourced under the [MIT License](LICENSE).

---

#  Thank You for Visiting!

Happy Coding! 

---
