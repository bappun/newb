from django.conf.urls import url

from newb.apps.shop import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^products/$', views.products, name="products"),
]