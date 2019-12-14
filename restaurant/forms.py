from django import forms
from .models import Area, Customer, About, Gallary, Reservation, Coupon
from django.contrib.auth.forms import UserCreationForm  # Form for signup
from django.contrib.auth.models import User  # Django default user table

class ReserveForm(forms.ModelForm):
    # name = forms.CharField(required=True, max_length=40, label='', widget=forms.TextInput(attrs={"class":"form-control style", "placeholder":"Your Name*"}))
    # phone = forms.CharField(required=True, max_length=11, label='', widget=forms.TextInput(attrs={"class":"form-control style", "placeholder":"Mobile Number*"}))
    # email = forms.EmailField(required=True, max_length=60, label='', widget=forms.EmailInput(attrs={"class":"form-control style", "placeholder":"Your Email*"}))
    # person = forms.IntegerField(required=True, label='', widget=forms.NumberInput(attrs={"class":"form-control style", "placeholder":"How many person?*"}))
    # date = forms.DateField(required=True, label='', widget=forms.DateInput(format="%m.%d.%Y", attrs={"class": "form-control datepicker-here style", "placeholder": "date*"}))
    # time = forms.TimeField(required=True, label='', widget=forms.TimeInput(attrs={"class": "form-control time-picker style", "placeholder": "time*"}))
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'email', 'person','date','time',]

class CouponForm(forms.ModelForm):
    code = forms.CharField( required=True, label='',widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}))

    class Meta:
        model = Coupon
        fields = ['code',]

class CustomerForm(forms.ModelForm):
    phn = forms.CharField(max_length=11, required=True,label='Phone Number', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}))
    location = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}))
    area_id = forms.ModelChoiceField(queryset=Area.objects.all().order_by('area_name'), required=False, label='Area')
    image = forms.ImageField(required=False)

    class Meta:
        model = Customer
        fields = ['phn', 'location', 'area_id','image']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class":"form-control","placeholder":""}))
    last_name = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(attrs={"class":"form-control","placeholder":""}))
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}))
    email = forms.EmailField(max_length=80,required=True,  widget=forms.TextInput(attrs={"class":"form-control","placeholder":""}))
    password1 = forms.CharField(max_length=20,required=True, label='Password', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":""}))
    password2 = forms.CharField(max_length=20, required=True, label='Repeat password', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": ""}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError("Password did n't match")
        return password1


