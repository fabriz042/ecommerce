from rest_framework import serializers
from .models import Product, Category, Status, Brand, Series, Character, Tag, Sport

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
class StatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="status.name")
    brand = serializers.CharField(source="brand.name")
    category = serializers.CharField(source="category.name")
    series = serializers.CharField(source="series.name", required=False)
    character = serializers.CharField(source="character.name", required=False)
    tags = serializers.StringRelatedField(many=True)
    sports = serializers.StringRelatedField(many=True) 
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'stock', 'description', 'slug',
            'weight', 'status', 'brand', 'category', 
            'series', 'character', 'tags', 'sports'
        ]
