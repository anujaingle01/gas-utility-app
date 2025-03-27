from django.http import HttpResponse  # ✅ Import HttpResponse

def register(request):
    return HttpResponse("User Registration API")  # ✅ Simple response for testing
