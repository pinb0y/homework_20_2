from django.contrib.gis.gdal.prototypes.srs import clone_srs
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_page.html'

def product_page(request, pk):
    product_name = Product.objects.get(pk=pk)

    context = {
        'title': 'товар',
        'object': product_name
    }
    return render(request, 'catalog/product_page.html', context)
