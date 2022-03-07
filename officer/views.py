#from attr import fields
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .forms import FineCreationForm
from .models import Fine, Location
import logging
from .filters import Fine_filter



def fine_create_view(request):  
    form = FineCreationForm()

    if request.method == 'POST':
        form = FineCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successful make new fine")
            return redirect('fine_add')
             
        else:
            messages.warning(request,"Invalid Data Enter")
    #console log
    #logger = logging.getLogger()
    #logger.propogate = True
    #logger.error(form)
    return render(request, 'officer/officer_index.htm', {'form': form})



def fine_update_view(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    form = FineCreationForm(instance=fine)
    if request.method == 'POST':
        form = FineCreationForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect('fine_change', pk=pk)
              
    return render(request, 'officer/officer_index.htm', {'form': form})


# AJAX
def load_locations(request):
    district_id = request.GET.get('district_id')
    locations = Location.objects.filter(district_id=district_id).all()
    return render(request, 'officer/lcoation_list_options.htm', {'locations': locations})
    #return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
def dashboard(request):
     return render(request, 'officer/dashboard.htm')

    

def offenceDetails(request):
     fines = Fine.objects.all()
     return render(request, 'officer/offence_details.htm',{'fines': fines})

#driver_infor(multyple valdue parameter)
def driver_info(request):
    finesd = Fine.objects.all()
    inforFilter = Fine_filter(request.GET, queryset=finesd)
    finesd = inforFilter.qs
    return render(request, 'officer/driver_infor.htm',{'inforFilter':inforFilter,'finesd':finesd})
        