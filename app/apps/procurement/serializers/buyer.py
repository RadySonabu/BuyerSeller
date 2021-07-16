from ..models import  Buyer
from rest_framework import serializers
from rest_framework import viewsets

class BuyerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Buyer 
		fields=['id', 'name', 'address', 'contact_number']