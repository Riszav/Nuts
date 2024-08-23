from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer, NewsDetailSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=["НОВОСТИ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ СПИСКА НОВОСТЕЙ'
    )
)
class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(tags=["НОВОСТИ"])
@extend_schema_view(
    get=extend_schema(
        summary='ДЕТАЛЬНЫЙ ПРОСМОТР НОВОСТЕЙ'
    )
)
class NewsDetailApiView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
