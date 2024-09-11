from django.urls import path
from . import views

app_name = 'nuts'

urlpatterns = [
    path('category_name/', views.CategoryNameListAPIView.as_view(), name='category-name-list'),
    path('category/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-retrieve'),
    path('hit_products/', views.ProductHitListAPIView.as_view(), name='product-list'),
    path('search_product/', views.ProductSearchListAPIView.as_view(), name='search-products'),
    path('recipe/', views.RecipeListAPIView.as_view(), name='recipe_list'),
 ]
