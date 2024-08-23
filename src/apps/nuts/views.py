from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from .models import Product, Category
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=["ПРОДУКТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ДЕТАЛЬНЫЙ ПРОСМОТР ПРОДУКТОВ'
    )
)
class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ВСЕХ КАТЕГОРИЙ С ПРОДУКТАМИ'
    )
)
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ОДНОЙ КАТЕГРИИ С ПРОДУКТАМИ'
    )
)
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'