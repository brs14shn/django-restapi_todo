from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import TodoSerializers, CategorySerializers
from .models import Category, Todo

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

#! CBV ##VİEWSET 👇

#! crud işlemlerinin hepsine izin veriyor...
class TodoModelViewSet(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers


#! CBV ##CONCRATE APIVİEW 👇
# get and post işlemi yapar
class CategoryListCreate(ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class=CategorySerializers


class CategoryConcrateURD(RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class=CategorySerializers
   lookup_field="pk"
