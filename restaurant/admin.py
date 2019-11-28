from django.contrib import admin
from .models import Events, Area, Customer, About, Gallary, Reservation, Food_Category, Menu, Order_Status,Coupon, Order, Ordered_food, Payment_Method, Payment, Position_List, Employee, Expense

# Register your models here.


class AreaModel(admin.ModelAdmin):
    list_display = ["__str__","is_delivaryAvailable"]
    search_fields = ["__str__"]

    class Meta:
        Model = Area


admin.site.register(Area, AreaModel)


class CustomerModel(admin.ModelAdmin):
    list_display = ["__str__", "name", "phn", "area_id"]
    search_fields = ["__str__","phn"]

    class Meta:
        Model = Customer


admin.site.register(Customer, CustomerModel)


class AboutModel(admin.ModelAdmin):
    list_display = ["__str__", "mobile","email","address"]
    search_fields = ["__str__"]

    class Meta:
        Model = About


admin.site.register(About, AboutModel)


class GallaryModel(admin.ModelAdmin):
    list_display = ["__str__","created_on"]
    search_fields = ["__str__"]

    class Meta:
        Model = Gallary


admin.site.register(Gallary, GallaryModel)


class ReservationModel(admin.ModelAdmin):
    list_display = ["__str__","phone","person","date","time"]
    search_fields = ["__str__"]

    class Meta:
        Model = Reservation


admin.site.register(Reservation, ReservationModel)


class Food_CategoryModel(admin.ModelAdmin):
    list_display = ["__str__", "from_time", "to_time","description"]
    search_fields = ["__str__"]
    list_per_page = 30

    class Meta:
        Model = Food_Category


admin.site.register(Food_Category, Food_CategoryModel)


class MenuModel(admin.ModelAdmin):
    list_display = ["__str__", "price", "is_available", "rating","category_id"]
    search_fields = ["__str__"]
    list_filter = ["name", "price","category_id"]

    class Meta:
        Model = Menu


admin.site.register(Menu, MenuModel)


class Order_StatusModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Order_Status


admin.site.register(Order_Status, Order_StatusModel)



class CouponModel(admin.ModelAdmin):
    list_display = ["__str__","type","amount","number_of_coupon","expire_date"]
    search_fields = ["__str__"]
    list_filter = ["type", "expire_date"]

    class Meta:
        Model = Coupon


admin.site.register(Coupon, CouponModel)



class OrderModel(admin.ModelAdmin):
    list_display = ["__str__","customer_id","delivary_address","note","order_status_id"]
    search_fields = ["__str__"]
    list_filter = ["customer_id", "order_status_id"]

    class Meta:
        Model = Order

admin.site.register(Order, OrderModel)



class Ordered_foodModel(admin.ModelAdmin):
    list_display = ["__str__","food_id","qty"]
    search_fields = ["__str__"]

    class Meta:
        Model = Ordered_food

admin.site.register(Ordered_food, Ordered_foodModel)



class Payment_MethodModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Payment_Method


admin.site.register(Payment_Method, Payment_MethodModel)


class PaymentModel(admin.ModelAdmin):
    list_display = ["__str__","order_id","method_id","amount","created_on"]
    search_fields = ["__str__"]
    list_filter = ["method_id"]

    class Meta:
        Model = Payment


admin.site.register(Payment, PaymentModel)


class Position_ListModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model = Position_List


admin.site.register(Position_List, Position_ListModel)


class EmployeeModel(admin.ModelAdmin):
    list_display = ["__str__","position","phone","sallary","address"]
    search_fields = ["__str__"]
    list_filter = ["position"]

    class Meta:
        Model = Employee


admin.site.register(Employee, EmployeeModel)


class ExpenseModel(admin.ModelAdmin):
    list_display = ["__str__","qty","cost","bought_by","created_on"]
    search_fields = ["__str__"]
    list_filter = ["bought_by"]

    class Meta:
        Model = Expense


admin.site.register(Expense, ExpenseModel)


class EventModel(admin.ModelAdmin):
    list_display = ["__str__", "date", "start_time", "end_time"]
    search_fields = ["__str__","date"]

    class Meta:
        Model = Events


admin.site.register(Events, EventModel)