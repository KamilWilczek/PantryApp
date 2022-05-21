from django.urls import reverse
from django.shortcuts import redirect, render

from .models import Item, ShoppingList
from .forms import ItemForm, ShoppingListForm

# Create your views here.
def shopping_list_list_view(request):
    qs = ShoppingList.objects.all
    context = {"shopping_lists": qs}
    return render(request, "shopping_list/list.html", context)


def shopping_list_create_view(request):
    form = ShoppingListForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "shopping_list/create-update.html", context)


def shopping_list_update_view(request, id=None):
    obj = ShoppingList.objects.get(id=id)
    form = ShoppingListForm(request.POST or None, instance=obj)
    context = {"form": form, "object": obj}
    if form.is_valid():
        form.save()
        context["message"] = "Data saved."
    return render(request, "shopping_list/create-update.html", context)


def shopping_list_delete_view(request, id=None):
    obj = ShoppingList.objects.get(id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        success_url = reverse("shopping_list:list")
        return redirect(success_url)
    context = {"object": obj}
    return render(request, "shopping_list/delete.html", context)


def item_update_view(request, id=None):
    obj = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=obj)
    context = {"form": form, "object": obj}
    if form.is_valid():
        form.save()
        context["message"] = "Data saved."
    return render(request, "shopping_list/create-update.html", context)
