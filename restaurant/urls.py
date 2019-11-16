from django.conf.urls import url
from restaurant import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
]