from datetime import datetime

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    # t = models.TextChoices()
    email = models.EmailField


class Seller(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()


class Order(models.Model):
    date = models.DateTimeField(default=datetime.now())
    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class Order_positions(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
