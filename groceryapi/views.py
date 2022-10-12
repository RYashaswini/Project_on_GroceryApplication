import imp
from django.shortcuts import render
from .models import CustomerModel,UnitModel,ProductModel,OrderDetailModel,OrderModel
from .serializer import OrderSeializer,OrderDetailSeializer, ProductSeializer, UnitSeializer,CustomerSeializer,ProductSeializerNN,OrderDetailSeializerNN,OrderSeializerNN,DataCount,NestlistSerializer
from rest_framework import generics 
from rest_framework.views import APIView  
from rest_framework.response import Response 
from rest_framework import status



# Create your views here.
class CustomerCreate(generics.ListCreateAPIView):
    
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSeializer
    
class CustomerUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSeializer
    
class UnitCreate(generics.ListCreateAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = UnitSeializer

class UnitUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = UnitSeializer

class ProductCreate(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSeializer

class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSeializer

class OrderDetilCreate(generics.ListCreateAPIView):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSeializer

class OrderDetailUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSeializer

class OrderCreate(generics.ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSeializer

class OrderUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSeializer

#Non Nested Serializer

class ProductNN(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSeializerNN

class ProductupdateNN(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSeializerNN

class OrderdetailNN(generics.ListCreateAPIView):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSeializerNN

class orderdetailupdateNN(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSeializerNN

#final list

class ListNN(generics.ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = NestlistSerializer

class ListupdateNN(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = NestlistSerializer

class OrderNN(APIView):

    def get(self,request):
        order = OrderModel.objects.all()
        serializer = OrderSeializerNN(order, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = OrderSeializerNN(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class OrderupdateNN(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSeializerNN


           


class DataCountGenerics(generics.ListAPIView):
    queryset=OrderModel.objects.all()
    serializer_class = DataCount
