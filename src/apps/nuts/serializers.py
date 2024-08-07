from rest_framework import serializers
from .models import Catalog, Category, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'volume', 'price']


class CatalogSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'image', 'hit_of_sales', 'prices']


class CategorySerializer(serializers.ModelSerializer):
    catalogs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'catalogs']

    def get_catalogs(self, obj):
        catalogs = obj.catalogs.all()[:8]
        return CatalogSerializer(catalogs, many=True).data