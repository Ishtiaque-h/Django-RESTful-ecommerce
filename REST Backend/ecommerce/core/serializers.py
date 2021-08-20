from rest_framework import serializers
from .models import ProductType, Product

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('id','title')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'pk', 'title', 'product_type', 'price', 'description', 'image','priority')


class ProductViewSerializer(serializers.ModelSerializer):
    product_type_title = serializers.CharField(source='product_type.title', read_only=True)

    class Meta:
        model = Product
        fields = ('pk', 'title', 'product_type', 'product_type_title', 'price', 'image')

class ProductDetailsSerializer(serializers.ModelSerializer):
    product_type_title = serializers.CharField(source='product_type.title', read_only=True)

    class Meta:
        model = Product
        fields = ('pk', 'title', 'description', 'product_type_title', 'price', 'image')