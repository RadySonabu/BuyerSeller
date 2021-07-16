from ..models import  Buyer
from rest_framework import viewsets
from ..serializers.buyer import *



class BuyerView(viewsets.ModelViewSet):
	queryset=Buyer.objects.all()
	serializer_class=BuyerSerializer