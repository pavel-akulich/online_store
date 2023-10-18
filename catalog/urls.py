from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, catalog_products, create_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog_products, name='catalog_products'),
    path('create_product/', create_product, name='create_product'),
]
