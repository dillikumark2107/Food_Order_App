from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username + " - " + self.food.name
