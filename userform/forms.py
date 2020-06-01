from django import forms
from .models import Bookingdetails1

class RegistrationForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'phone'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookingdetails1
        fields = ['first_name','last_name','user_name','email','phone','startdate','enddate','address1','hotel1','room1']

    
    

