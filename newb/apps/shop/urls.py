from django.conf.urls import url
from django.contrib.auth import views as auth_views

from newb.apps.shop import views
from newb.apps.shop.forms import AuthForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shop/checkout/(?P<id>[0-9]+)/$', views.shop_checkout, name='shop_checkout'),
    url(r'^shop/checkout/done/$', views.shop_checkout_done, name='shop_checkout_done'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='shop/login.html', authentication_form=AuthForm), name='login'),
    url(r'^authentication/$', views.authentication, name='authentication'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/$', views.account, name='account'),
    url(r'^contact/$', views.contact, name='contact'),
]