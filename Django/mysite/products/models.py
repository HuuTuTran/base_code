from django.db import models

# Create your models here.
class manufacturer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    color = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(manufacturer,on_delete=models.CASCADE)


