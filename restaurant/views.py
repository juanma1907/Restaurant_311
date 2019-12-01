from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Events, Area, Customer, About, Gallary, Reservation, Food_Category, Menu, Order_Status,Coupon, Order, Ordered_food, Payment_Method, Payment, Position_List, Employee, Expense
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .forms import ContactForm, SignUpForm, PostForm, CouponForm, FeaturedPostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve
from .forms import ReserveForm


# views function that will interact with frontend
def index(request):
    food = Menu.objects.filter(is_available=True).prefetch_related('category_id').order_by('name')
    category = Food_Category.objects.filter().order_by('-created_on')
    event = Events.objects.filter().order_by('-date')[:2]
    about = About.objects.only('address')[:1]
        # name = request.POST.get('name')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # person = request.POST.get('person')
        # date = request.POST.get('date')
        # time = request.POST.get('time')
        #
        # form = form(name=name, phone=phone, email=email, person=person, date=date, time=time )
        # form.save()
    context = {
        'about' :about,
        'event' : event,
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
    food = Menu.objects.filter().prefetch_related('category_id').order_by('name')
    category = Food_Category.objects.filter().order_by('-created_on')
    context={
        'food' : food,
        'category' : category
    }
    return render(request,'menu.html',context)


def reservation(request):
    form = ReserveForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully submitted reservation request.")
        return redirect('index')
    else:
        messages.error(request, "Sorry. Reservation request failed. Try again")
        return  redirect('reservation')

    return render(request,'reservation.html', {'form':form})

def shop(request):
    return render(request,'shop.html')


def shop_single(request, id):
    food = get_object_or_404(Menu, id=id)
    related = Menu.objects.filter(category_id=food.category_id).exclude(id=food.id)[:4]
    context = {
        'food' : food,
        'related' :related
    }
    return render(request,'shop-single.html', context)


def login(request):
    return render(request,'sign-in.html')


def signup(request):
    return render(request,'sign-up.html')


def logout(request):
    logout(request)
    return redirect('index')