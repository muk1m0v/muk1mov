from .models import Shops, Debts
from rest_framework import viewsets

class ShopSerializer(viewsets.ModelViewSet):
    class Meta:
        model = Shops
        fields = ['title','owner_name']

class DebtSerializer(viewsets.ModelViewSet):
    class Meta:
        model = Debts
        fields = ['name','price','phone','shop']