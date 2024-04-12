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
        model = Teacher
        fields = '__all__'        
