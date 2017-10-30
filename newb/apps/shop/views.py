from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from newb.apps.shop.forms import CustomerRegisterForm, ContactForm, UserRegisterForm
from .models import VideoGame, Order


def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


def shop(request):
    context = {
        'products': VideoGame.objects.all()
    }
    return render(request, 'shop/shop.html', context)


@login_required(login_url='/login/')
def shop_checkout(request, id):
    context = {
        'product': VideoGame.objects.get(id=id)
    }
    return render(request, 'shop/shop_checkout.html', context)


@login_required(login_url='/login/')
def shop_checkout_done(request):
    if request.method == 'POST':
        product = VideoGame.objects.get(id=request.POST.get("product-id"))
        order = Order(customer=request.user.customer, item=product)
        order.save()
        return redirect('shop:account')

    return redirect('shop:index')


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
        user_form = UserRegisterForm(request.POST, prefix="user_form")
        customer_form = CustomerRegisterForm(request.POST, prefix="customer_form")

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()

            user.customer.user_id = user.id
            user.customer.address = customer_form.cleaned_data.get('address')
            user.customer.postal_code = customer_form.cleaned_data.get('postal_code')
            user.customer.city = customer_form.cleaned_data.get('city')
            user.customer.country = customer_form.cleaned_data.get('country')
            user.customer.phone = customer_form.cleaned_data.get('phone')

            user.save()

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

    else:
        user_form = UserRegisterForm()
        user_form.prefix = "user_form"
        customer_form = CustomerRegisterForm()
        customer_form.prefix = "customer_form"

    context = {'user_form': user_form, 'customer_form': customer_form}
    return render(request, 'shop/register.html', context)


@login_required(login_url='/login/')
def account(request):
    context = {
        'orders': Order.objects.filter(customer=request.user.customer),
    }
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

