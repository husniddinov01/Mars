from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

class Register(APIView):
    def post(self, request):
        serializer = AdminSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        admin = Admin.objects.filter(username = username, password = password).first()
        if admin:
            serializer = AdminSerializer(student)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)            


class AdminGroupView(APIView):
    def get(self, request,id):
        admin = Admin.objects.filter(id=id).first()
        if admin:
            serializers = AdminSerializer(admin)
            return Response(serializers.data)
        else:
            return Response('SORRY error')
        
    
    def patch(self, request, id):
        admin = Admin.objects.filter(id=id).first()
        if admin:
            serializers = AdminSerializer(instance = admin,data = request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('SORRY Admin NOT FOUND!')



    def delete(self, request, id):
        admin = Admin.objects.filter(id=id).first()
        if admin:
            admin.delete()
            return Response('GROUP DELETED!')
        else:
            return Response('SORRY GROUP NOT FOUND! ')
# Create your views here.
