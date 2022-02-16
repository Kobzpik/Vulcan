from django.shortcuts import render,get_object_or_404
from officer.models import Fine
from authenticate.models import Driver


# Create your views here.
def index(request):
        return render(request, 'driver/index_driver.htm')
        
def fine_list(request,pk):
        fined = Fine.objects.filter(driver_id = pk)     
        finedh = Driver.objects.get(user_id = pk)
        return render(request, 'driver/fines_list.htm',{'fined': fined,'finedh':finedh})


