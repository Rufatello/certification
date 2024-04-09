from django.urls import path

from shop.apps import ShopConfig
from shop.views import FactoryCreateApiView
app_name = ShopConfig.name

urlpatterns = [
    path('shop/create/', FactoryCreateApiView.as_view(), name='shop-create'),
]