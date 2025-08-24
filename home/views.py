import logging
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseServerError
# from .models import Restaurant
# Create your views here.
logger = logging.getLogger(__name__)

def home(request):
    try:
        context={
            "restaurant_name": "My Restaurant",
            "restaurant_phone": getattr(settings, "RESTAURANT_PHONE", "Not Available")
        }
        return render(request, "home.html", context)
    except Exception as e:
        logger.error(f"Error remdering homepage: {e}", exc_info=True)
        return HttpResponseServerError("Something went wrong while loading the homepage.")


def menu_list(request):
    try:
        context = {
            "menu_items": [
                {"id": 1, "name": "Pizze", "price":199},
                {"id": 2, "name": "Paneer", "price": 299},
                {"id": 3, "name": "Burger", "price": 99},
                {"id": 4, "name": "coffee", "price": 129},
            ]
        }
        return render(request, "menu.html", context)
    except Exception as e:
        logger.error(f"Error rendering menu list: {e}", exc_info=True)
        return HttpResponseServerError("Something went wrong while loading the menu.")
        
def about(request):
    restaurant_name = getattr(setting, "RESTAURANT_NAME", "Our Restaurant")
   return render(request, 'about.html',{"restaurant_name": restaurant_name})   


def contact(request):
    try:
        context = {
            "restaurant_name": "My Reataurant",
            # "restaurant_phone": getattr(settings, "RESTAURANT_PHONE, "Not Available"),
        }
        return render(request, "contact.html", context)
    except Exception as e:
        logger.error(f"Error rendering contact page: {e}", exc_info=True)
        return HttpResponseServerError("Something went wrong while loading t.he contact page")