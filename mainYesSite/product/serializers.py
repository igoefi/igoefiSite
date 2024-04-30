from rest_framework import serializers
from .models import Category, Product

class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thrumbnail'
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerialiser(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'products',
        )