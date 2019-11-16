from django.conf.urls import url
from restaurant import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error404, name='error404'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>', views.blog_single, name='blog_single'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('gallary/', views.gallary, name='gallary'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug>', views.shop_single, name='shop_single'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

]