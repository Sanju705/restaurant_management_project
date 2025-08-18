from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Restaurant
# Create your views here.
def home(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    return render(request, "home.html", {"restaurant_name": restaurant_name})


class MenuItemView(APIView):

    def get(self, request):
        menu_item = [
            {"id": 1, "name": "pizze", "price":199},
            {"id": 2, "name": "paneer", "price": 299},
            {"id": 3, "name": "Burger", "price": 99},
            {"id": 4, "name": "coffee", "price": 129},
        ]
        return Response (menu_item, status=status.HTTP_200_OK)
         