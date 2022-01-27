from django.urls import reverse
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
#from sqlalchemy import true
from .form import OfficerSignUpForm, DriverSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'authenticate/home.htm')

def profile_officer(request):
    return render(request, 'authenticate/profile.htm')

def profile_driver(request):
    return render(request, 'driver/index_driver.htm')

class driver_register(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'authenticate/driver_register.htm'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login_driver')

class officer_register(CreateView):
    model = User
    form_class = OfficerSignUpForm
    template_name = 'authenticate/officer_register.htm'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login_police')


#def login_request(request):
    #if request.method=='POST':
       # form = AuthenticationForm(data=request.POST)
        #if form.is_valid():
            #username = form.cleaned_data.get('username')
           # password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #if user is not None :
              #  login(request,user)
               # return redirect('profile')
           # else:
              #  messages.error(request,"Invalid username or password")
       # else:
              #  messages.error(request,"Invalid username or password")
   # return render(request, 'authenticate/login_1.htm',
    #context={'form':AuthenticationForm()})
    
def login_requestDriver(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_driver== True :
                login(request,user)
                return redirect('profile_driver')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'authenticate/login_1.htm',
    context={'form':AuthenticationForm()})
    
def login_requestPolice(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_officer== True :
                login(request,user)
                return redirect('profile_officer')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'authenticate/login_police.htm',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


