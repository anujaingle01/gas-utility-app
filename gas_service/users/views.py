# from rest_framework.generics import CreateAPIView
# from .serializers import UserSerializer
# from .models import CustomUser

# class RegisterUserView(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer



from django.http import JsonResponse

def register_user(request):
    return JsonResponse({"message": "User registered successfully"})
