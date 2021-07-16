from ..models import  Transaction
from rest_framework import serializers
from rest_framework import viewsets

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction 
		fields=['id', 'transaction_type', 'item_id', 'quantity_in_kg', 'amount']