from django.shortcuts import render

from .models import VideoGame


def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


def products(request):
    context = {
        'products': VideoGame.objects.all()
    }
    return render(request, 'shop/products.html', context)
