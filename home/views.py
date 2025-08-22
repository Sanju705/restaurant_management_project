from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Restaurant
# Create your views here.
def home(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    return render(request, "home.html", {"restaurant_name": restaurant_name})


def menu_list(request):
        menu_items = [
            {"id": 1, "name": "pizze", "price":199},
            {"id": 2, "name": "paneer", "price": 299},
            {"id": 3, "name": "Burger", "price": 99},
            {"id": 4, "name": "coffee", "price": 129},
        ]
        return render(request, "menu.html", {"menu_items": menu_items})
        
def about(request):
    restaurant_name = getattr(setting, "RESTAURANT_NAME", "Our Restaurant")
   return render(request, 'about.html',{"restaurant_name": restaurant_name})   