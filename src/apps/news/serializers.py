from rest_framework import serializers
from .models import News
from config import services


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'image']


class NewsDetailSerializer(serializers.ModelSerializer, services.ManyImagesServices):
    images = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'images', 'date']

    def get_images(self, obj):
        request = self.context.get('request')
        return self.get_images_list(obj, request, obj.news_images)
