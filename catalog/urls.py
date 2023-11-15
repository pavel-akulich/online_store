from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactPageView, ProductListView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog_products'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('view_product/<int:pk>/', cache_page(90)(ProductDetailView.as_view()), name='view_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
