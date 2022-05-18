from django.shortcuts import render

from .models import Item

# Create your views here.
def item_list_view(request):
    qs = Item.objects.all
    context = {"items_list": qs}
    return render(request, "shopping_list/list.html", context)
