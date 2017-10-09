from django.conf.urls import url
from django.contrib.auth import views as auth_views

from newb.apps.shop import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^login/$',  auth_views.LoginView.as_view(template_name='shop/login.html'), name="login"),
    url(r'^authentication/$', views.authentication, name="authentication"),
    url(r'^signout/$', views.signout, name="signout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^account/$', views.account, name="account"),
    url(r'^contact/$', views.contact, name="contact"),
]