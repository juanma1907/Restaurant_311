from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from .models import Events, Area, Customer, About, Gallary, Reservation, Food_Category, Menu, Order_cart, Order_Status,Coupon, Order, Ordered_food, Payment_Method, Payment, Position_List, Employee, Expense
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max,Count, Sum, F
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .forms import ContactForm, SignUpForm, PostForm, CouponForm, FeaturedPostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve
from .forms import ReserveForm, SignUpForm
from django.utils.timezone import datetime


# views function that will interact with frontend
def index(request):
    food = Menu.objects.filter(is_available=True).prefetch_related('category_id').order_by('name')
    category = Food_Category.objects.filter().order_by('-created_on')
    event = Events.objects.filter().order_by('-date')[:2]
    about = About.objects.only('address')[:1]
    #cart widget
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        cart_item = Order_cart.objects.filter(customer_id=user.id).prefetch_related('food_id').order_by('-created_on')
    totalBill=sum(i.food_id.price*i.qty for i in cart_item)
    itemCount = Order_cart.objects.filter(customer_id=user.id).aggregate(no_of_item=Count('food_id'))
    context = {
        'totalBill':totalBill,
        'itemCount':itemCount,
        'cart_item': cart_item,
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
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        customer = get_object_or_404(Customer, name=user)
        cart_item = Order_cart.objects.filter(customer_id=user.id).prefetch_related('food_id').order_by('-created_on')
        totalBill = sum(i.food_id.price * i.qty for i in cart_item)
        area_list=Area.objects.filter(is_delivaryAvailable=True).order_by('area_name')
        context = {
            'totalBill': totalBill,
            'cart_item': cart_item,
            'area_list': area_list,
            'customer':customer
        }
        return render(request,'checkout.html', context)
    else:
        return render(request, 'sign-in.html')


def coupon(request):
    if request.user.is_authenticated:
        activeCoupon = Coupon.objects.filter(number_of_coupon__gt=0, expire_date__gt=datetime.now())
        if request.method == "POST":
            user_coupon = request.POST.get('coupon_code')
            is_valid = False
            usedCoupon =0
            usedCouponPercnt=0.00
            for i in activeCoupon:
                if i.code==user_coupon:
                    if i.Amount_Type == "F":
                        usedCoupon=i.amount
                    else:
                        usedCouponPercnt=i.amount/100
                    is_valid=True
                    break
            if is_valid:
                context={
                    'usedCoupon':usedCoupon,
                    'usedCouponPercnt':usedCouponPercnt
                }
                return render(request, 'checkout2.html',context)
            else:
                messages.add_message(request, messages.ERROR, "Wrong/Expired Coupon code")
        return render(request, 'checkout.html')
    else:
        return render(request, 'sign-in.html')

def cart(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        cart_item = Order_cart.objects.filter(customer_id=user.id).prefetch_related('food_id').order_by('-created_on')
    totalBill=sum(i.food_id.price*i.qty for i in cart_item)
    context = {
        'totalBill':totalBill,
        'cart_item': cart_item,
    }
    return render(request,'shop-cart.html', context)

def contact(request):
    return render(request,'contact-us.html')


def gallary(request):
    pic = Gallary.objects.only("title", "image").order_by('-created_on')
    return render(request,'gallery.html',{'pic':pic})


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
        instance =form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS, "Your Reservation request submit successfully.")
        return redirect('reservation')
    return render(request,'reservation.html', {"form":form})


def shop(request):
    food = Menu.objects.filter(is_available=True).prefetch_related('category_id').order_by('name')
    category = Food_Category.objects.filter().order_by('-created_on')
    # ==========Search==========
    search = request.GET.get('q')
    if search:
        food = food.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )
    context = {
        'food': food,
        'category': category
    }
    return render(request,'shop.html', context)


def shop_category(request, name):
    getcategory = get_object_or_404(Food_Category, name=name)
    food = Menu.objects.filter(category_id=getcategory.id)
    category = Food_Category.objects.filter().order_by('-created_on')
    context = {
        'food' : food,
        'category' :category
    }
    return render(request,'shop.html', context)


def shop_single(request, id):
    food = get_object_or_404(Menu, id=id)
    related = Menu.objects.filter(category_id=food.category_id).exclude(id=food.id)[:4]
    context = {
        'food' : food,
        'related' :related
    }
    return render(request,'shop-single.html', context)



def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, "Username or Password Mismatch")

    return render(request,'sign-in.html')


def getsignup(request):
    if request.method == "GET":
        form = SignUpForm(request.POST or None)
        return render(request, "sign-up.html", {"form": form})
    else:
        form = SignUpForm(request.POST)
        first_name = request.POST.get("first_name")

        first_name = first_name.lower()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = True
            usr = User.objects.all()
            newFirstName = first_name.replace(" ", "")
            i = 0
            for u in usr:
                if u.username == newFirstName or u.username == newFirstName + str(i):
                    i = i + 1
                else:
                    pass
            if i == 0:
                instance.username = newFirstName
            else:
                instance.username = newFirstName + str(i)
            instance.save()
            return HttpResponse("<h1>Congratulations! You are registered.</h1> <br> <h2>Your username is: <b>"+newFirstName+"</b></h2><br> <a href='/login'><button type='button'>Login</button><a>")
        else:
            return redirect("signup")


def getlogout(request):
    logout(request)
    return redirect('index')


def lostpass(request):
    return render(request,'lost-password.html')


def add_to_cart(request, fid):
    if request.user.is_authenticated:
        Reguser = get_object_or_404(User, id=request.user.id)
        added_food = get_object_or_404(Menu, id=fid)
        userCart = Order_cart.objects.filter(customer_id=Reguser.id)
        isExists=False;
        for i in userCart:
            if i.food_id.id == fid:
                isExists=True
                break
        if not isExists:
            obj_instance = Order_cart.objects.create(
                customer_id=Reguser,
                food_id=added_food,
                qty=1
            )
        return redirect('index')
    else:
        return redirect('login')


def cart_Update_increase(request, fid):
    if request.user.is_authenticated:
        Reguser = get_object_or_404(User, id=request.user.id)
        added_food = get_object_or_404(Menu, id=fid)
        item = get_object_or_404(Order_cart, customer_id=Reguser.id, food_id__id=fid)

        item.qty=F('qty')+1
        item.save(update_fields=['qty'])
        return redirect('cart')
    else:
        return redirect('login')


def cart_Update_decrease(request, fid):
    if request.user.is_authenticated:
        Reguser = get_object_or_404(User, id=request.user.id)
        added_food = get_object_or_404(Menu, id=fid)
        item = get_object_or_404(Order_cart, customer_id=Reguser.id, food_id__id=fid)
        if item.qty>1:
            item.qty=F('qty')-1
            item.save(update_fields=['qty'])
        else:
            messages.add_message(request, messages.ERROR, "To delete, click the cross button from left.")
        return redirect('cart')
    else:
        return redirect('login')

def add_to_cart_Delete(request, fid):
    if request.user.is_authenticated:
        Reguser = get_object_or_404(User, id=request.user.id)
        item = get_object_or_404(Order_cart, food_id=fid)
        item.delete()
        return redirect('index')
    else:
        return redirect('login')