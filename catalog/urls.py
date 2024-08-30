from django.urls import path
from catalog.apps import CatalogConfig
from catalog.models import Product
from catalog.views import ProductListView, ProductDetailView, toggle_activity, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product_page/<int:pk>', ProductDetailView.as_view(), name='product_page'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
    path('create/', ProductCreateView.as_view(), name='create_product')
]
