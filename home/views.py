from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def home(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    return render(request, "home.html", {"restaurant_name": Q restaurant})