from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from newb.apps.shop.forms import CustomerRegisterForm
from .models import VideoGame


def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


def shop(request):
    context = {
        'products': VideoGame.objects.all()
    }
    return render(request, 'shop/products.html', context)


def authentication(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.customer.address = form.cleaned_data.get('address')
            user.customer.postal_code = form.cleaned_data.get('postal_code')
            user.customer.city = form.cleaned_data.get('city')
            user.customer.country = form.cleaned_data.get('country')
            user.customer.phone = form.cleaned_data.get('phone')
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

    else:
        form = CustomerRegisterForm()

    context = {'form': form}
    return render(request, 'shop/register.html', context)


@login_required(login_url='/login/')
def account(request):
    context = {}
    return render(request, 'shop/account.html', context)


def contact(request):
    context = {}
    return render(request, 'shop/contact.html', context)

