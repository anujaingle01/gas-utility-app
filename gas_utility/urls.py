"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.http import HttpResponse  # Import HttpResponse to create a basic homepage
from django.contrib import admin  # Import Django's admin module
from django.urls import path, include  # Import path and include

# Define a simple home view that returns a basic response
def home(request):
    return HttpResponse("Welcome to Gas Utility App!")

# Define the URL patterns
urlpatterns = [
    path('', home),  # ✅ Handles the home page (http://127.0.0.1:8000/)
    path('admin/', admin.site.urls),  # ✅ Admin panel URL
    path('api/users/', include('users.urls')),  # ✅ Include URLs from accounts app
    path('api/requests/', include('requests.urls')),  # ✅ Includes requests app URLs
]




