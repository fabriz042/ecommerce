from rest_framework import serializers
from .models import Product, Category, State, Brand, Series, Character, Tag, Sport, ProductImage

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class StateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
class SeriesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class CharacterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class SportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url', 'alt_text', 'is_main']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Serializer for searching and listing products quickly
class ProductListSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="state.name")
    images = ImageProductSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['slug', 'name', 'price', 'state', 'images']

# Detailed serializer for a single product
class ProductDetailSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="state.name")
    brand = serializers.CharField(source="brand.name")
    category = serializers.CharField(source="category.name")
    series = serializers.CharField(source="series.name", required=False)
    character = serializers.CharField(source="character.name", required=False)
    tags = serializers.StringRelatedField(many=True)
    sports = serializers.StringRelatedField(many=True) 
    images = ImageProductSerializer(many=True)
     
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'stock', 'description', 'slug',
            'weight', 'state', 'brand', 'category',
            'series', 'character', 'tags', 'sports', 'images'
        ]