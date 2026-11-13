from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Shops, Debts
from .serializers import ShopSerializer, DebtSerializer


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

    def gettt(self):
        return Shops.objects.filter(user=self.request.user)

    def create_users(self, serializer):
        serializer.save(user=self.request.user)

class DebtViewSet(viewsets.ModelViewSet):
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated]

    def gett(self):
        all_data = self.request.data
        shop = Shops.objects.filter(title=all_data.get('title'))
        debt = Debts.objects.filter(shop=shop)
        return debt

    def create_debt(self, serializer):
        serializer.save()