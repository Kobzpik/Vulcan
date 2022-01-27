from django.shortcuts import render
from officer.models import Fine, Location
from authenticate.models import Driver

# Create your views here.
def index(request):
        return render(request, 'driver/index_driver.htm')
def fine_list(request):
        fined = Fine.objects.all() 
        driverd = Driver.objects.all() 
        return render(request, 'driver/fines_list.htm',{'fined': fined,'driverd': driverd})