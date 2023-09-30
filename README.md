# Python_Web_II_step_task
# Book_Giveaway_Service_API
Book Giveaway Service API
This is a simple Django-based API for a book giveaway service. This project includes user authentication, CRUD operations for books, and API documentation using Swagger.


# Table of Contents
  Requirements
  Installation
  Docker Setup
  Run the Application
  API Documentation (Swagger)

# Requirements
  Python 3.x
  Django 4.x
  Docker
  PostgreSQL (or any database you prefer)

# Setup virtual environment (Optional if you're using Docker)
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
  pip install -r requirements.txt

#  < Docker Setup >
# Build the Docker image
  docker build -t bookgiveawayservice .

# Run the Docker container
  docker run -p 8000:8000 bookgiveawayservice


#  < Run the Application >
# Apply migrations
  python manage.py migrate

# Run the server
  python manage.py runserver

# <<< API Documentation >>>
We use drf_yasg for API documentation which is accessible at http://127.0.0.1:8000/swagger/.

# To set this up:
# Install the package
  pip install drf-yasg

INSTALLED_APPS = [
    # ... other apps
    'users',
    'drf_yasg',
    'rest_framework',
]


#    <<< Update urls.py >>>
 Add Swagger URLs to your urls.py.


from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # ... other URL patterns
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

