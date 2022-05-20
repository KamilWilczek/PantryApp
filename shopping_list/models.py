from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class ItemCategory(models.TextChoices):
    FRUITS_VEGETABLES = "fruits and vegetables"
    MEAT = "meat"
    DIARY = "diary"
    DRY_GOODS = "dry good"
    ALCOHOLS = "alcohols"
    MEDICINE = "medicine"
    PET_GOODS = "pet goods"
    BABY_GOODS = "baby goods"
    DOMESTIC_DETERGENTS = "domestic detergents"
    READY_COOK_MEALS = "ready-cook meals"
    HYGIENE = "hygiene"
    COFFEE_TEA = "coffee & tea"
    FROZEN_FOODS = "frozen foods"
    GARDEN_TINKER = "garden and tinkering"
    BREAD = "bread"
    PRESERVES = "preserves"
    SPICES = "spices, sauces, additives"
    FISH = "fishes and seafood"
    SWEETS = "sweets and snacks"
    FATS = "fats"
    DRINKS = "water and drinks"
    NUTS = "dried fruit and nuts"
    HERBS = "fresh herbs"
    CANS = "canned food"
    OTHER = "other"


class ItemUnit(models.TextChoices):
    PIECES = "pcs"
    PACKAGES = "pkgs"
    KILOGRAM = "kg"
    GRAM = "g"
    LITER = "l"
    MILLILITER = "ml"


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(
        max_length=20, choices=ItemUnit.choices, null=True, blank=True
    )
    category = models.CharField(max_length=25, choices=ItemCategory.choices)
    note = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ["complete"]

    def get_absolute_url(self):
        return reverse("shopping_list:list")
