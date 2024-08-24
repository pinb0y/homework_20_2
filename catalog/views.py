from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная',
    }
    return render(request, 'catalog/index.html', context)


def product_page(request, pk):
    product_name = Product.objects.get(pk=pk)

    context = {
        'title': 'товар',
        'object': product_name
    }
    return render(request, 'catalog/product_page.html', context)
