from django.shortcuts import render
from .models import list

# Create your views here.
def index(request):
        return render(request, 'TVDM/index.htm')
       
def userform(request):
        data=list.objects.all()
        test={"test_data":data}
        return render(request, 'route.htm',test)
            
 