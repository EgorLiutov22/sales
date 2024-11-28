from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField


class Item(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()


class Order(models.Model):
    date = models.DateTimeField()
    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Positions(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
