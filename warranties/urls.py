from django.conf.urls import url
from . import views

app_name = "warranty"
urlpatterns = [
    url(r'^$', views.wrtyList, name="list"),
    url(r'^(?P<pk>[0-9]+)/$', views.wrtyDetail, name="detail"),
]
