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


def login(request):
    context = {}
    return render(request, 'shop/login.html', context)


def logout(request):
    context = {}
    return render(request, 'shop/logout.html', context)


def register(request):
    context = {}
    return render(request, 'shop/register.html', context)


def account(request):
    context = {}
    return render(request, 'shop/account.html', context)


def contact(request):
    context = {}
    return render(request, 'shop/contact.html', context)

