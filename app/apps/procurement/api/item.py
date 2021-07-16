from ..models import  Item
from rest_framework import viewsets
from ..serializers.item import *



class ItemView(viewsets.ModelViewSet):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer