from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.NewsListApiView.as_view()),
    path('news/<int:pk>/', views.NewsDetailApiView.as_view()),
 ]
