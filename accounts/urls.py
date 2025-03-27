# from django.urls import path
# from .views import register_user  # Import your view

# urlpatterns = [
#     path('register/', register_user, name='register_user'),
# ]




from django.urls import path  # ✅ Import path for URL patterns
from . import views  # ✅ Import views from the same app

urlpatterns = [
    path('register/', views.register, name='register'),  # ✅ Correct URL pattern
]
