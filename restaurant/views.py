from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Area, Customer, About, Gallary, Reservation, Food_Category, Menu, Order_Status,Coupon, Order, Ordered_food, Payment_Method, Payment, Position_List, Employee, Expense
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .forms import ContactForm, SignUpForm, PostForm, CouponForm, FeaturedPostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve


# views function that will interact with frontend
def index(request):
    food = Menu.objects.filter(is_available=True).prefetch_related('category_id').order_by('name')
    category = Food_Category.objects.filter().order_by('-created_on')
    #blog_post=
    context = {
        'food' : food,
        'category' : category
    }
    return render(request,'index.html',context)


def error404(request):
    return render(request,'404.html')


def about(request):
    return render(request,'about-us.html')


def blog(request):
    return render(request,'blog.html')


def blog_single(request):
    return render(request,'blog-single.html')


def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return render(request,'contact-us.html')


def gallary(request):
    return render(request,'gallery.html')


def menu(request):
    return render(request,'menu.html')


def reservation(request):
    return render(request,'reservation.html')

def shop(request):
    return render(request,'shop.html')


def shop_single(request):
    return render(request,'shop-single.html')


def login(request):
    return render(request,'sign-in.html')


def signup(request):
    return render(request,'sign-up.html')


def logout(request):
    logout(request)
    return redirect('index')