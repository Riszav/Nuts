from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import News
from .serializers import NewsSerializer


# Create your views here.
class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

