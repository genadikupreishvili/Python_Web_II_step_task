from django.contrib.auth.views import LogoutView
from .views import profile
from .views import book_list, add_book, update_book, delete_book
from .views import MyLoginView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'books', views.BookViewSet)



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('books/add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('add_condition/', views.add_condition, name='add_condition'),
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    path('api/', include(router.urls)),


]

