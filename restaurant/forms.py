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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter first name"}))
    last_name = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter last name"}))
    email = forms.EmailField(max_length=254,required=True,  widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    password1 = forms.CharField(max_length=20,required=True, label='Password', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
    password2 = forms.CharField(max_length=20, required=True, label='Repeat password', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter password"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
