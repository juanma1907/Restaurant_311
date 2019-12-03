from django import forms
from .models import Area, Customer, About, Gallary, Reservation
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