from django.conf.urls import url

from newb.apps.shop import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^products/$', views.products, name="products"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^account/$', views.account, name="account"),
    url(r'^contact/$', views.contact, name="contact"),
]