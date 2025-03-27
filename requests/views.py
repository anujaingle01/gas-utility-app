from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def request_list(request):
    if request.method == "GET":
        data = [
            {"id": 1, "name": "Gas Connection Request", "description": "Request for new gas connection"},
            {"id": 2, "name": "Cylinder Refill", "description": "Request to refill the gas cylinder"}
        ]
        return JsonResponse({"requests": data}, safe=False)  # ✅ Return JSON response




