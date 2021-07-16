from ..models import  Item
from rest_framework import serializers
from rest_framework import viewsets

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item 
		fields=['id', 'name', 'description', 'selling_price_per_kg']