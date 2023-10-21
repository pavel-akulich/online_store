from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactPageView, ProductListView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog_products'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
]
