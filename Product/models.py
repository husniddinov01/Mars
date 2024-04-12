from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =200)
    model = models.CharField(max_length =200)
    about = models.CharField(max_length =200)
    category = models.CharField(max_length =200)
    gbjoy = models.CharField(max_length =200)
    image = models.ImageField(upload_to = 'products/')
    price = models.IntegerField()
    quantity = models.IntegerField()
    color = models.CharField(max_length =200)

    def __str__(self):
        return self.name   