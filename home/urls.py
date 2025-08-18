from django.urls import path
from .views import *

urlpatterns = [
    path ("", home, name="home"),
    path("menu-item/", MenuItemListView.as_view(), name="menu-item"),
]