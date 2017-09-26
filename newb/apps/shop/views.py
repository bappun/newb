from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


def products(request):
    context = {}
    return render(request, 'shop/products.html', context)
