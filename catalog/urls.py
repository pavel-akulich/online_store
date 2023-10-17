from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, catalog_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog_products, name='catalog_products'),
]
