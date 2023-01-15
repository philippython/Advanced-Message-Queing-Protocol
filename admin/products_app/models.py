from django.db import models

# Create your models here.

class Products(models.Model):
    title= models.CharField(max_length=280)
    image= models.CharField(max_length=280)
    likes= models.PositiveIntegerField(default=0)


class USer(models.Model):
    pass