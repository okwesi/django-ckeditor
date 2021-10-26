from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    url('view/', views.Homeview.as_view(), name="view"),
    url('^$', views.home, name='home')
]
