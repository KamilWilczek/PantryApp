# Generated by Django 4.0.4 on 2022-05-18 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('pcs', 'pcs'), ('pkgs', 'pkgs'), ('kg', 'kg'), ('g', 'g'), ('l', 'l'), ('ml', 'ml')], max_length=20, null=True)),
                ('category', models.CharField(choices=[('FV', 'fruits and vegetables'), ('MT', 'meat'), ('D', 'diary'), ('DG', 'dry goods'), ('ALC', 'alcohols'), ('MED', 'medicine'), ('PG', 'pet goods'), ('BG', 'baby goods'), ('DD', 'domestic detergents'), ('RCM', 'ready-cook meals'), ('H', 'hygiene'), ('CT', 'coffee & tea'), ('FF', 'frozen foods'), ('GT', 'garden and tinkering'), ('B', 'bread'), ('PV', 'preserves'), ('S', 'spices, sauces, additives'), ('FS', 'fishes and seafood'), ('SS', 'sweets and snacks'), ('F', 'fats'), ('WD', 'water and drinks'), ('DFN', 'dried fruit and nuts'), ('FH', 'fresh herbs'), ('CF', 'canned food'), ('O', 'other')], max_length=10)),
                ('note', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['complete'],
            },
        ),
    ]