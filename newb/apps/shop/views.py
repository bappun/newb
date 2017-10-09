from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from newb.apps.shop.forms import CustomerRegisterForm, ContactForm
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


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


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
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            contact.name = form.cleaned_data.get('name')
            contact.subject = form.cleaned_data.get('subject')
            contact.message = form.cleaned_data.get('message')
            contact.save()

            if contact is not None:
                return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'shop/contact.html', context)

