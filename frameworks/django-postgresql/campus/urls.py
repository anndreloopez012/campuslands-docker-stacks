from django.http import JsonResponse
from django.urls import path

def home(_request):
    return JsonResponse({"stack": "Django + PostgreSQL", "status": "ok"})

urlpatterns = [path("", home)]
