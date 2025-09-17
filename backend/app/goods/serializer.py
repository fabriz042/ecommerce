from rest_framework import serializers
from .models import (Bag, Airgear, Attribute, Oil, Trophy, Glove)

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'
class BagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'
class AirgearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airgear
        fields = '__all__'
class AirgearDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airgear
        fields = '__all__'
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'
class AttributeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'
class OilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oil
        fields = '__all__'
class OilDetailSerializer(serializers.ModelSerializer):
    attributes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Oil
        fields = '__all__'
class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = '__all__'
class TrophyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = '__all__'
class GloveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glove
        fields = '__all__'
class GloveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glove
        fields = '__all__'
