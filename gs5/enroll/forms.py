from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Customer

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirmed Password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']

