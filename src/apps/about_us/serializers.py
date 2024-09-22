from rest_framework import serializers
from .models import AboutUs, Banner


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['text', 'image']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['image', 'video', 'mobi_image']
