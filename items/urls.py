from django.conf.urls import url
from . import views

app_name = "item"
urlpatterns = [
    url(r'^$', views.itemList, name="list"),
    url(r'^(?P<pk>[0-9]+)/$', views.itemDetail, name="detail"),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.itemEdit, name="edit"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.itemDelete, name="delete"),
    url(r'^add/$', views.itemAdd, name="add"),
]
