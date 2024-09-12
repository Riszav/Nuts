from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from .models import AboutUs, Banner
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=["О НАС"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ТЕКСТА И ФОТОГРАФИИ'
    )
)
class AboutUsAPIView(RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.first()
        serializer = self.serializer_class(queryset).data
        return Response(serializer, 200)


@extend_schema(tags=["БАННЕР"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ИЗОБРАЖЕНИЯ ИЛИ ВИДЕО ДЛЯ БАННЕРА'
    )
)
class BannerAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.first()
        serializer = self.serializer_class(queryset).data
        return Response(serializer, 200)
