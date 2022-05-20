from django.shortcuts import redirect, render

from .models import Item
from .forms import ItemForm

# Create your views here.
def item_list_view(request):
    qs = Item.objects.all
    context = {"items_list": qs}
    return render(request, "shopping_list/list.html", context)


def item_create_view(request):
    form = ItemForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "shopping_list/create-update.html", context)


def item_update_view(request, id=None):
    obj = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=obj)
    context = {"form": form, "object": obj}
    if form.is_valid():
        form.save()
        context["message"] = "Data saved."
    return render(request, "shopping_list/create-update.html", context)
