from django.urls import path
from . import views

app_name = 'about_us'

urlpatterns = [
    path('about_us/', views.AboutUsAPIView.as_view(), name='about_us'),
    path('banner/', views.BannerAPIView.as_view(), name='banner'),
]
