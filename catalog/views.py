from django.contrib.gis.gdal.prototypes.srs import clone_srs
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'price', 'image')
    success_url = reverse_lazy('catalog:index')


def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:index'))

