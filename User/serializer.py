from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LoginStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['login', 'password'] 


class TeacherSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class LoginTeacherSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'        



class GrupSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'        


class HomeWorkSeriaizer(serializers.ModelSerializer):
    class  Meta:
         model = HomeWork
         fields = '__all__'      


class CoinsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = '__all__'        


class HackatonSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Hackaton
        fields = '__all__'        
