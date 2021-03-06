# Generated by Django 4.0.4 on 2022-05-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0002_alter_item_category_alter_item_unit_shoppinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shopping_list',
            field=models.ManyToManyField(to='shopping_list.shoppinglist'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('fruits and vegetables', 'Fruits Vegetables'), ('meat', 'Meat'), ('diary', 'Diary'), ('dry goods', 'Dry Goods'), ('alcohols', 'Alcohols'), ('medicine', 'Medicine'), ('pet goods', 'Pet Goods'), ('baby goods', 'Baby Goods'), ('domestic detergents', 'Domestic Detergents'), ('ready-cook meals', 'Ready Cook Meals'), ('hygiene', 'Hygiene'), ('coffee & tea', 'Coffee Tea'), ('frozen foods', 'Frozen Foods'), ('garden and tinkering', 'Garden Tinker'), ('bread', 'Bread'), ('preserves', 'Preserves'), ('spices, sauces, additives', 'Spices'), ('fishes and seafood', 'Fish'), ('sweets and snacks', 'Sweets'), ('fats', 'Fats'), ('water and drinks', 'Drinks'), ('dried fruit and nuts', 'Nuts'), ('fresh herbs', 'Herbs'), ('canned food', 'Cans'), ('other', 'Other')], max_length=25),
        ),
    ]
