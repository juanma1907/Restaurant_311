from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class Area (models.Model):
    area_name = models.CharField(max_length=30)
    is_delivaryAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.area_name


class Customer (models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phn = models.CharField(db_index=True, max_length=11, unique=True)
    location = models.TextField(max_length=50)
    area_id = models.ForeignKey(Area, on_delete=None)
    image = models.ImageField(default='default', upload_to='pro_pics', blank=True)
    rating = models.IntegerField()
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name.username


class About(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    logo = models.ImageField(default='default', upload_to='Others', blank=True)
    mobile = models.CharField(max_length=12)
    address = models.TextField(max_length=70)
    open_time = models.TimeField()
    close_time = models.TimeField()
    holiday = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Gallary(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(default='default', upload_to='gallary', blank=True)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=60)
    person = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Food_Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image_small = models.ImageField(default='default', upload_to='others', blank=True)
    image_cover = models.ImageField(default='default', upload_to='others', blank=True)
    from_time = models.TimeField()
    to_time = models.TimeField()
    description = models.TextField(max_length=200)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField(max_length=200)
    is_available = models.BooleanField(db_index=True, default=True)
    rating = models.IntegerField()
    image = models.ImageField(default='default', upload_to='menu', blank=True)
    category_id = models.ForeignKey(Food_Category, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Order_Status(models.Model):
    status = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.status


class Coupon(models.Model):
    PERCENTAGE = 'P'
    FLAT = 'F'
    Amount_Type = (
        (PERCENTAGE, 'Percentage'),
        (FLAT, 'Flat'),
    )
    code = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=1, choices=Amount_Type, default=PERCENTAGE)
    amount = models.FloatField()
    expire_date = models.DateTimeField()
    number_of_coupon = models.IntegerField()

    def __str__(self):
        return self.code


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=None)
    delivary_address = models.TextField(max_length=70)
    note = models.TextField(max_length=100)
    coupon_id = models.OneToOneField(Coupon, on_delete=models.CASCADE)
    order_status_id = models.ForeignKey(Order_Status, on_delete=None)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.customer_id.id


class Order_cart(models.Model):
    customer_id = models.ForeignKey(User, on_delete=None)
    food_id = models.ForeignKey(Menu, on_delete=None)
    qty = models.IntegerField()
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.customer_id.username


class Ordered_food(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Menu, on_delete=None)
    qty = models.IntegerField()

    def __str__(self):
        return self.order_id.id


class Payment_Method(models.Model):
    method_name = models.CharField(max_length=15)

    def __str__(self):
        return self.method_name


class Payment(models.Model):
    order_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    method_id = models.ForeignKey(Payment_Method, on_delete=None)
    amount = models.FloatField()
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.order_id


class Position_List(models.Model):
    position_name = models.CharField(max_length=30)

    def __str__(self):
        return self.position_name


class Employee(models.Model):
    name = models.CharField(max_length=35)
    phone = models.CharField(db_index=True, max_length=11, unique=True)
    email = models.EmailField(max_length=50)
    sallary = models.FloatField()
    position = models.ForeignKey(Position_List, on_delete=None)
    address = models.TextField(max_length=70)
    image = models.ImageField(default='default', upload_to='pro_pics', blank=True)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    item = models.CharField(max_length=100)
    qty = models.FloatField()
    cost = models.FloatField()
    bought_by = models.ForeignKey(Employee, on_delete=None)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.item


class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(max_length=600)
    image = models.ImageField(default='default', upload_to='event_pic', blank=True)
    created_on = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title