
from django.urls import path
from . import views  # ✅ Make sure 'views' is imported

urlpatterns = [
    path('register/', views.register, name='register'),  # ✅ Ensure this path is present
]
