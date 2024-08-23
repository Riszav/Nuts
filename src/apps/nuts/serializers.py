from rest_framework import serializers
from .models import Product, Category, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'volume', 'price']


class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'hit_of_sales', 'prices']


class CategorySerializer(serializers.ModelSerializer):
    catalogs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'catalogs']

    def get_catalogs(self, obj):
        catalogs = obj.catalogs.all()[:8]
        return ProductSerializer(catalogs, many=True).data