from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ProductEditView(APIView):

    def get(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            serializer = ProdcutSerializer(product)
            return Response(serializer.data)
        else:
            return Response("Bunday mahsulot topilmadi")
        


    def patch(self, request, id):
        
        if product:
            serializer = ProdcutSerializer(instace = product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serialzier.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Bunday mahsulot topilmadi")
  

    def delete(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            product.delete()
            return Response("O'chirildi")
        else:
            return Response("Bunday mahsulot topilmadi")



class GetallView(APIView):
    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProdcutSerializer(products, many = True)
            return Response(serializer.data)
        else:
            return Response("Malumot topilmadi")




