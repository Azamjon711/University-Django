from django.db import models


class Customers(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)