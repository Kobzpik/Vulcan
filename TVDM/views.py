from django.shortcuts import render
from .models import list

# Create your views here.
def home(request):
        return render(request, 'index.htm')
       
def userform(request):
        data=list.objects.all()
        test={"test_data":data}
        return render(request, 'route.htm',test)
            
 