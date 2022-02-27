from django.urls import reverse
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
#from sqlalchemy import true
from .form import OfficerSignUpForm, DriverSignUpForm,CodeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User , Codes , Officer
from officer.models import Fine
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'authenticate/home.htm')

@login_required
def profile_officer(request):
    return render(request, 'authenticate/profile.htm')

@login_required
def profile_driver(request):
    fines = Fine.objects.all()
    return render(request, 'driver/index_driver.htm',{'fines':fines})

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
        return redirect('officer_register')
     


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

#driver login authentication       
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
                messages.warning(request,"Invalid username or password")
        else:
                messages.warning(request,"Invalid username or password")
    return render(request, 'authenticate/login_1.htm',
    context={'form':AuthenticationForm()})

#officer login authentication   
def login_requestPolice(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_officer== True :
                login(request,user)
                request.session['pk'] = user.pk
                return redirect('verify')
                #return redirect('profile_officer')
            else:
                messages.warning(request,"Invalid username or password")
        else:
                messages.warning(request,"Invalid username or password")
    return render(request, 'authenticate/login_police.htm',
    context={'form':AuthenticationForm()})

#veriry police through OTP authentcate
def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = Codes.objects.get(pk=pk)
        userp = Officer.objects.get(pk=pk)
        code = user.number
        code_user = f"{user.user}:{user.number}"
        if not request.POST:
                print(code_user)
                #send_sms(code_user, userp.phone_number)
        if form.is_valid():
                num = form.cleaned_data.get('number')
                print("this is code "+num)
                if code == num:
                        #code.save()
                        #login(request, user)
                        return redirect('profile_officer')
                else:
                        messages.warning(request,('Invalid OTP code'))

    return render(request, 'authenticate/verify.htm',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/authenticate/home')


