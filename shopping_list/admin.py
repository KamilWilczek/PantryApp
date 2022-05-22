from django.contrib import admin

from .models import Item, ShoppingList

# Register your models here.
class ShoppingListItemInline(admin.StackedInline):
    model = Item.shopping_list.through
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [ShoppingListItemInline]
    readonly_fields = ["created", "updated"]
    exclude = ("shopping_list",)


class ShoppingListAdmin(admin.ModelAdmin):
    inlines = [ShoppingListItemInline]
    readonly_fields = ["created", "updated"]


admin.site.register(Item, ItemAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)
