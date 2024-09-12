from rest_framework import serializers
from .models import News
from . import services


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'image']


class NewsDetailSerializer(serializers.ModelSerializer, services.NewsServices):
    images = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'images', 'date']
