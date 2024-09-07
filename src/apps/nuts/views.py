from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from .models import Product, Category, Recipe
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from config.pagination import CustomPageNumberPagination


@extend_schema(tags=["ТОПОВЫЕ ПРОДУКТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ТОЛЬКО ТОПОВЫХ ПРОДУКТОВ '
    )
)
class ProductHitListAPIView(ListAPIView):
    queryset = Product.objects.filter(hit_of_sales=True)
    serializer_class = ProductSerializer


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ВСЕХ КАТЕГОРИЙ С ПРОДУКТАМИ'
    )
)
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ НАЗВАНИЯ ВСЕХ КАТЕГОРИЙ ДЛЯ ФУТЕРА'
    )
)
class CategoryNameListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryNameSerializer
    pagination_class = None


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ОДНОЙ КАТЕГРИИ С ПРОДУКТАМИ'
    )
)
class CategoryDetailAPIView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs['pk'])
        queryset = self.queryset.filter(category=category)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "name": category.name,
                "catalogs": serializer.data
            })
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "name": category.name,
            "catalogs": serializer.data
        }, status=200)


@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ВСЕХ РЕЦЕПТОВ'
    )
)
class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = None