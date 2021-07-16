from ..models import  Seller
from rest_framework import viewsets
from ..serializers.seller import *



class SellerView(viewsets.ModelViewSet):
	queryset=Seller.objects.all()
	serializer_class=SellerSerializer