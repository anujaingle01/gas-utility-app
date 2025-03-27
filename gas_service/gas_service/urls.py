from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple Home Page Function
def home(request):
    return HttpResponse("<h1>Welcome to Gas Service API</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Your users app URLs
    path('api/service_requests/', include('service_requests.urls')),  # Your service requests app URLs
    path('', home),  # Default home page
]
