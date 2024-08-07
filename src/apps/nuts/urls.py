from django.urls import path
from . import views

app_name = 'nuts'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('catalog/', views.CatalogListView.as_view(), name='product-list'),
 ]
