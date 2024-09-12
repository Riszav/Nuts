from rest_framework import serializers
from .models import Product, Category, Price, Recipe
from decouple import config
from .utils import ProductWhatsAppLinkGenerator


class PriceSerializer(serializers.ModelSerializer):
    order_link = serializers.SerializerMethodField()
     
    class Meta:
        model = Price
        fields = ['id', 'volume', 'price', 'order_link']

    def get_order_link(self, obj):
        admin_number = self.context.get('admin_number', config('DEFAULT_WHATSAPP_NUMBER'))
        return ProductWhatsAppLinkGenerator.generate_whatsapp_link(obj, admin_number)


class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'hit_of_sales', 'prices']


class ProductHitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'hit_of_sales',]


class CategorySerializer(serializers.ModelSerializer):
    catalogs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'catalogs']

    def get_catalogs(self, obj):
        catalogs = obj.catalogs.all()[:8]
        return ProductSerializer(catalogs, many=True).data


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'product_title', 'description', 'image', 'link']
