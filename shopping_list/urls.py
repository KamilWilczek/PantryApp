from django.urls import path

from .views import item_list_view

app_name = "shopping_list"

urlpatterns = [path("", item_list_view, name="list")]
