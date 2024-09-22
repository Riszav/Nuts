from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from .models import Product, Category, Recipe
from src.apps.generals.models import WhatsAppNumber
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework import filters
from rest_framework.response import Response
from config.pagination import CustomPageNumberPagination
from decouple import config
from django.db.models import Prefetch
from rest_framework.permissions import AllowAny


@extend_schema(tags=["ПОИСК"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ СПИСКА ПРОДУКТОВ ',
        description='Возвращает список всех доступных продуктов с возможностью поиска и фильтрации.',
        parameters=[
            OpenApiParameter(name='search', description='Поиск по названию продукта', required=False, type=OpenApiTypes.STR)
        ],
        responses={
            200: ProductSerializer(many=True),
            400: OpenApiResponse(description='Неверный запрос')
        }
    )
)
class ProductSearchListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_ru', 'name_en']


    def get_serializer_context(self):
        context = super().get_serializer_context()
        admin_number = WhatsAppNumber.objects.first()
        context['admin_number'] = admin_number.number if admin_number else config('DEFAULT_WHATSAPP_NUMBER')
        return context


@extend_schema(tags=["ТОПОВЫЕ ПРОДУКТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ТОЛЬКО ТОПОВЫХ ПРОДУКТОВ '
    )
)
class ProductHitListAPIView(ListAPIView):
    queryset = Product.objects.filter(hit_of_sales=True).order_by('id')
    serializer_class = ProductHitSerializer


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ВСЕХ КАТЕГОРИЙ С ПРОДУКТАМИ'
    )
)
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.prefetch_related(Prefetch('catalogs', queryset=Product.objects.prefetch_related('prices'))).all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny,]
    pagination_class = None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        admin_number = WhatsAppNumber.objects.first()
        context['admin_number'] = admin_number.number if admin_number else config('DEFAULT_WHATSAPP_NUMBER')
        return context

@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ НАЗВАНИЯ ВСЕХ КАТЕГОРИЙ ДЛЯ ФУТЕРА'
    )
)
class CategoryNameListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryNameSerializer
    pagination_class = None


@extend_schema(tags=["КАТЕГОРИЯ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ОДНОЙ КАТЕГРИИ С ПРОДУКТАМИ'
    )
)
class CategoryDetailAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related('prices').all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    lookup_field = 'pk'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        admin_number = WhatsAppNumber.objects.first()
        context['admin_number'] = admin_number.number if admin_number else config('DEFAULT_WHATSAPP_NUMBER')
        return context

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


@extend_schema(tags=["РЕЦЕПТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ВСЕХ РЕЦЕПТОВ'
    )
)
class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer
    pagination_class = None

    
@extend_schema(tags=["РЕЦЕПТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ДЕТАЛЬНЫХ РЕЦЕПТОВ'
    )
)
class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    lookup_field = 'pk'