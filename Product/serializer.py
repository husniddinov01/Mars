from rest_framework import serializers
from .models import *

class ProdcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'




         