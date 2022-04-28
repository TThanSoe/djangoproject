from django.db import models
import datetime

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=50)
    unit_price = models.FloatField(default=0.0)


def __str__(self):
    return self.unit + " " + self.quantity + " " + self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(default=datetime.date.today)
