from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_title'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'item_id',
            'title',
            'href',
            'current_price',
            'old_price',
            'brand',
            'category',
            'sell_status'
        )


class IdStorageSerializer(serializers.Serializer):
    product_ids = serializers.CharField()


