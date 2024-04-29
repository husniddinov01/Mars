from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import datetime
from rest_framework import generics


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class LoginView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        student = Student.objects.filter(login = login, password = password).first()
        if student:
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RegisterTeacherView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeacherSeriaizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class LoginTeacherView(APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')
        user = Teacher.objects.filter(login = login, password = password).first()
        if user:
            return Response('success')
        else:
            return Response('fail')   




class CreateGroupView(APIView):
    def post(self,request):
        serializers = GrupSeriaizer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


    def get(self,request):
        groups = Group.objects.all()
        if groups:
            serializers = GrupSeriaizer(groups, many=True)
            return Response(serializers.data)
        else:
            return Response('SORY NOT GROUP CRATE OZIN')


class EditGroupView(APIView):
    def get(self, request,id):
        group = Group.objects.filter(id=id).first()
        if group:
            serializers = GrupSeriaizer(group)
            return Response(serializers.data)
        else:
            return Response('SORRY error')
        
    
    def patch(self, request, id):
        group = Group.objects.filter(id=id).first()
        if group:
            serializers = GrupSeriaizer(instance = group,data = request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('SORRY GROUP NOT FOUND!')



    def delete(self, request, id):
        group = Group.objects.filter(id=id).first()
        if group:
            group.delete()
            return Response('GROUP DELETED!')
        else:
            return Response('SORRY GROUP NOT FOUND! ')



 
class HomeWorkView(APIView):
    def post (self, request):
        serializers = HomeWorkSeriaizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Respose (serializers.data)
        else:
            return Respose (serializers.errors)
    def get (self, request):
        homework = HomeWork.objects.all()
        if  homework:
            serializers = HomeWorkSeriaizer(homework, many = True)
            return Response(serializers.data)
        else:
            return  Response("NO homework found")   


class HomeWorGroupView(APIView):
    def get(self, request,id):
        homewor = homewor.objects.filter(id=id).first()
        if homewor:
            serializers = HomeWorkSeriaizer(homewor)
            return Response(serializers.data)
        else:
            return Response('SORRY error')



    def delete(self, request, id):
            homewor = HomeWork.objects.filter(id=id).first()
            if homewor:
                homewor.delete()
                return Response('GROUP DELETED!')
            else:
                return Response('SORRY HomeWork NOT FOUND! ')



class  HomeWorEditView(APIView):
    def post (self, request, id):
        homework = HomeWork.objects.filter(id=id).first()
        if homework:
            homework.file = request.data.get('file')
            diedline = int( homework.time) + 3
            if homework.time <= datetime.datetime.today and datetime.datetime <= diedline:
                homework.save()
                return Response('YUKLANDI')  
            else:
                return Response('Chopildiz, vaqtida yuklash kerak!')
        else:
            return Response ('Bunday uyga vazifa topilmadi')            



class PostCoinView(APIView):
    def post(self, request):
        serializers = CoinsSeriaizer(data = request.data)
        id = request.data.get('student')
        coins = request.data.get('coins')
        student = Student.objects.filter(id=id).first()
        if student:
            if serializers.is_valid():
                student.coin += coins
                student.save()
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)

class HackatonView(generics.CreateAPIView):
    serializer_class = HackatonSeriaizer
    queryset = Hackaton.objects.all()



class  HackatonGetView(generics.ListAPIView):
    serializer_class = HackatonSeriaizer
    queryset = Hackaton.objects.all()


class EditHackatonView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HackatonSeriaizer
    queryset = Hackaton.objects.all()
    lookup_field = 'id'