# Lab 3.1 & 3.2 – REST API for Student Management System
**IT322 | Student ID: 2023300660**

A fully-featured Django REST API for managing students in a university system, implementing:
- ✅ **Lab 3.1** – REST API Design & Implementation (CRUD)
- ✅ **Lab 3.2** – JWT Authentication, Swagger Documentation & Debugging

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg
```

### 2. Run Migrations
```bash
python manage.py makemigrations students
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```
Or use the pre-seeded credentials: **admin / admin1234**

### 4. Start the Server
```bash
python manage.py runserver
```

---

## 🔑 Authentication (Lab 3.2 – Part A)

This API uses **JWT (JSON Web Token)** authentication via `djangorestframework-simplejwt`.

### Step 1: Obtain Tokens
```http
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin1234"
}
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### Step 2: Use Token in Requests
```http
GET /api/v1/students/
Authorization: Bearer <access_token>
```

### Step 3: Refresh Token
```http
POST /api/token/refresh/
Content-Type: application/json

{ "refresh": "<refresh_token>" }
```

---

## 📡 API Endpoints (Lab 3.1 – Part D & E)

**Base URL:** `http://localhost:8000/api/v1/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/students/` | List all students (paginated) |
| `POST` | `/api/v1/students/` | Create a new student |
| `GET` | `/api/v1/students/{id}/` | Retrieve a specific student |
| `PUT` | `/api/v1/students/{id}/` | Fully update a student |
| `PATCH` | `/api/v1/students/{id}/` | Partially update a student |
| `DELETE` | `/api/v1/students/{id}/` | Delete a student |

### Pagination Example
```
GET /api/v1/students/?page=1
```

### API Versioning
All endpoints are prefixed with `/api/v1/` for versioning.

---

## 📋 Sample Requests (Lab 3.1 – Part F)

### Create a Student (POST)
```json
{
  "student_id": "2024-001",
  "full_name": "Juan Dela Cruz",
  "email": "juan@student.edu",
  "course": "BSIT",
  "year_level": 3
}
```

### Expected Response (201 Created)
```json
{
  "id": 1,
  "student_id": "2024-001",
  "full_name": "Juan Dela Cruz",
  "email": "juan@student.edu",
  "course": "BSIT",
  "year_level": 3
}
```

---

## 📚 API Documentation (Lab 3.2 – Part C)

**Swagger UI:** http://localhost:8000/swagger/
**ReDoc:** http://localhost:8000/redoc/

---

## 🗂 Project Structure

```
lab3.1_rest_api_it322_2023300660/
├── student_api/
│   ├── settings.py        # Django config w/ DRF, JWT, Swagger, Logging
│   └── urls.py            # Root URL config (API + JWT + Swagger)
├── students/
│   ├── models.py          # Student model
│   ├── serializers.py     # StudentSerializer
│   ├── views.py           # StudentViewSet (CRUD + logging)
│   └── urls.py            # students/urls with DefaultRouter
├── manage.py
└── db.sqlite3
```

---

## 🔒 Security Testing (Lab 3.2 – Part D)

- Without a token → `401 Unauthorized`
- With valid token → `200 OK`
- With expired token → `401 Unauthorized` (use `/api/token/refresh/`)

---

## 🐛 Debugging (Lab 3.2 – Part D)

Logging is configured in `settings.py`. All student view actions are logged:
```
[2024-01-01 10:00:00] INFO students.views: Student list accessed by user: admin
[2024-01-01 10:00:05] WARNING students.views: Deleting student record 3 by user: admin
```
