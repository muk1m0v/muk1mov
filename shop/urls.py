from rest_framework.routers import DefaultRouter
from .views import ShopViewSet,DebtViewSet

router = DefaultRouter()
router.register('shops', ShopViewSet, basename='shop')
router.register('debts', DebtViewSet, basename='debts')

urlpatterns = router.urls
