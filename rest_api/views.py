from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Method which defines queryset to get products' data from database"""
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        
        if category is not None:
            """ Filter by given category param """
            queryset = queryset.filter(category=category)
        
        return queryset

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()