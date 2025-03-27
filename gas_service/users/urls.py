

from django.urls import path
from .views import register_user  # ✅ Import the function

urlpatterns = [
    path('register/', register_user, name='register'),  # ✅ Define the route
]
