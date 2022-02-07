from rest_framework import serializers
from rest_framework.mixins import CreateModelMixin

from shop.models import Item


class ItemSerializer(serializers.ModelSerializer, CreateModelMixin):
    """Сериализатор записи"""
    class Meta:
        model = Item
        fields = '__all__'
