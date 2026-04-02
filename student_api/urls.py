"""
student_api URL Configuration

Endpoints:
  /api/v1/students/           - Student CRUD (JWT protected)
  /api/token/                 - Obtain JWT access + refresh tokens
  /api/token/refresh/         - Refresh JWT access token
  /swagger/                   - Swagger UI (interactive API docs)
  /redoc/                     - ReDoc API documentation
  /admin/                     - Django admin panel
"""
from django.contrib import admin
from django.urls import path, include

# JWT Token views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger / OpenAPI documentation
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version='v1',
        description=(
            "A REST API for managing students in a university system.\n\n"
            "## Authentication\n"
            "This API uses **JWT (JSON Web Token)** authentication.\n\n"
            "1. POST `/api/token/` with valid credentials to obtain tokens.\n"
            "2. Include the access token in requests as:\n"
            "   `Authorization: Bearer <access_token>`\n\n"
            "## Pagination\n"
            "List endpoints are paginated. Use `?page=<n>` query parameter.\n"
            "Default page size: 10 records."
        ),
        contact=openapi.Contact(email="admin@university.edu"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # Root URL redirect to swagger docs
    path('', RedirectView.as_view(url='/swagger/', permanent=False), name='index'),

    # Django admin
    path('admin/', admin.site.urls),

    # API v1 - Students endpoints
    path('api/v1/', include('students.urls')),

    # JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
