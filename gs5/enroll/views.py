from django.shortcuts import render
from .forms import SignUpForm,EditUserProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'enroll/usercreationform.html',{'form':fm})

def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfull')

                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else: 
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST)
            if fm.is_valid():
                messages.success(request,'Profile Data Saved!! ')
                fm.save()
                return HttpResponseRedirect('/address/')
        else:
            fm = EditUserProfileForm(instance=request.user) 
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_add(request):
        return render(request,'enroll/address.html',{'name':request.user})
   
