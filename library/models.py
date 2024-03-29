from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()

