from django.shortcuts import render, HttpResponse, get_object_or_404, redirect


# views function that will interact with frontend
def index(request):
    return render(request,'index.html')


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