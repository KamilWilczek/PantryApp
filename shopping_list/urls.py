from django.urls import path

from .views import item_list_view, item_create_view, item_update_view

app_name = "shopping_list"

urlpatterns = [
    path("", item_list_view, name="list"),
    path("create-update/", item_create_view, name="create"),
    path("<int:id>/edit/", item_update_view, name="update"),
]
