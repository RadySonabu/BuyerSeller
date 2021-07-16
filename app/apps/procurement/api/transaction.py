from ..models import  Transaction
from rest_framework import viewsets
from ..serializers.transaction import *



class TransactionView(viewsets.ModelViewSet):
	queryset=Transaction.objects.all()
	serializer_class=TransactionSerializer