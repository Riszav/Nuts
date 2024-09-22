from rest_framework import serializers
from .models import Product, Category, Price, Recipe
from decouple import config
from config import services
from urllib.parse import urlencode
from config.settings.base import MODELTRANSLATION_LANGUAGES
from django.utils.translation import activate, gettext as _



class PriceSerializer(serializers.ModelSerializer):
    order_link = serializers.SerializerMethodField()
     
    class Meta:
        model = Price
        fields = ['id', 'volume', 'price', 'order_link']

    def get_order_link(self, obj):
        base_url = "https://api.whatsapp.com/send"
        number = self.context.get('admin_number', config('DEFAULT_WHATSAPP_NUMBER'))
#        message = _(f"Hello, I want to order ") + f"\"{obj.product.name}\". " + _("Price: ") + f"{obj.price}. " + _("Volume: ") + f"{obj.volume}"
        params = {'phone': number}
        return f"{base_url}?{urlencode(params)}"


class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'hit_of_sales', 'prices']


class ProductHitSerializer(serializers.ModelSerializer, services.ManyImagesServices):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images', 'hit_of_sales',]

    def get_images(self, obj):
        request = self.context.get('request')
        return self.get_images_list(obj, request, obj.catalog_images)
    

class CategorySerializer(serializers.ModelSerializer):
    catalogs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'catalogs']

    def get_catalogs(self, obj):
        catalogs = obj.catalogs.all()[:8]
        return ProductSerializer(catalogs, many=True, context=self.context).data


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'product_title', 'description', 'image']

        
class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'product_title', 'description', 'image', 'link']
