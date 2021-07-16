from ..models import  Seller
from rest_framework import serializers
from rest_framework import viewsets

class SellerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seller 
		fields=['id', 'name', 'address', 'contact_number']