
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.buyer import BuyerView
from .api.seller import SellerView
from .api.item import ItemView
from .api.transaction import TransactionView

router = DefaultRouter()

router.register("buyer", BuyerView)
router.register("seller", SellerView)
router.register("item", ItemView)
router.register("transaction", TransactionView)


urlpatterns = [path("", include("rest_framework.urls")),path("api/", include(router.urls)),]