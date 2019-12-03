from django.conf.urls import url
from restaurant import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error404, name='error404'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.blog_single, name='blog_single'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('gallary/', views.gallary, name='gallary'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('shop/', views.shop, name='shop'),
    path('shop/cat/<name>', views.shop_category, name='shop_category'),
    path('shop/<int:id>', views.shop_single, name='shop_single'),
    path('login/', views.getlogin, name='login'),
    path('lostPassword/', views.lostpass, name='lostpass'),
    path('logout/', views.getlogout, name='logout'),
    path('signup/', views.getsignup, name='signup'),

]