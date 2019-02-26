from django.conf.urls import url
from . import views

app_name = "item"
urlpatterns = [
    url(r'^$', views.itemList, name="list"),
    url(r'^(?P<pk>[0-9]+)/$', views.itemDetail, name="detail"),
]
