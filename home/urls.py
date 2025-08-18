from django.urls import path
from .views import MenuItemView

urlpatterns = [
    path("menu-item/", MenuItemListView.as_view(), name="menu-item"),
]