from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length  = 200)
    lastname = models.CharField(max_length  = 200)
    phone = models.CharField(max_length  = 200)
    password = models.CharField(max_length  = 200)
    login = models.CharField(max_length  = 200)
    parent = models.TextField()
    coin = models.IntegerField()
    day = models.IntegerField() 

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    lev = (('Backend', 'Backend'),
           ('Frontend', 'Frontend'),
           ('Starter', 'Starter'),
           ('Designer', 'Designer'))
    level = models.CharField(max_length=200, choices=lev)
    day = models.BooleanField(default=False)



    def __str__(self):
        return self.last_name
    


class Group(models.Model):
    name = models.TextField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    room = models.CharField(max_length=200)




    def __str__(self):
        return self.name