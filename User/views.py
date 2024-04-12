from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

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