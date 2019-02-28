from django.conf.urls import url
from . import views

app_name = "customer"
urlpatterns = [
    url(r'^$', views.customerList, name="list"),
    url(r'^add/$', views.customerAdd, name="add"),
    url(r'^(?P<pk>[0-9]+)/$', views.customerDetail, name="detail"),
    # url(r'^edit/(?P<pk>[0-9]+)/$', views.itemEdit, name="edit"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.customerDelete, name="delete"),
    # url(r'^add/$', views.itemAdd, name="add"),
]