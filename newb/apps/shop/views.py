from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from newb.apps.shop.forms import CustomerRegisterForm, ContactForm, UserRegisterForm
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
        form_user = UserRegisterForm(request.POST)
        form_customer = CustomerRegisterForm(request.POST)

        if form_user.is_valid() and form_customer.is_valid():
            user = form_user.save()
            user.customer = form_customer.save()
            user.save()
            user.customer.save()

            raw_password = form_user.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

    else:
        form_user = UserRegisterForm()
        form_customer = CustomerRegisterForm()

    context = {'form_user': form_user, 'form_customer': form_customer}
    return render(request, 'shop/register.html', context)


@login_required(login_url='/login/')
def account(request):
    context = {}
    return render(request, 'shop/account.html', context)


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_instance = form.save()
            contact_instance.name = form.cleaned_data.get('name')
            contact_instance.subject = form.cleaned_data.get('subject')
            contact_instance.message = form.cleaned_data.get('message')
            contact_instance.save()

            if contact_instance is not None:
                context['success'] = "Message envoyé !"
                form = ContactForm()

    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'shop/contact.html', context)

