from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length  = 200)
    parol = models.CharField(max_length  = 200)

    def __str__(self):
        return self.username
# Create your models here.
