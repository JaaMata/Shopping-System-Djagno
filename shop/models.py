from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500, null=True)
    img = models.ImageField(upload_to="item_image", null=True)

    def __str__(self):
        return self.name
