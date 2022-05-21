from django.contrib import admin

from .models import Item, ShoppingList

# Register your models here.
class ShoppingListAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]


admin.site.register(Item)
admin.site.register(ShoppingList, ShoppingListAdmin)
