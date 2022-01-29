#from attr import fields
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .forms import FineCreationForm
from .models import Fine, Location



def fine_create_view(request):
   
    form = FineCreationForm()
    if request.method == 'POST':
        form = FineCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fine_add')
        else:
            messages.error(request,"Invalid Data Enter")
        
    #stud = Fine.objects.all()    
    return render(request, 'officer/officer_index.htm', {'form': form})



def fine_update_view(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    form = FineCreationForm(instance=fine)
    if request.method == 'POST':
        form = FineCreationForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect('fine_change', pk=pk)
    else:
            messages.error(request,"Invalid Data Enter!")
              
    return render(request, 'officer/officer_index.htm', {'form': form})


# AJAX
def load_locations(request):
    district_id = request.GET.get('district_id')
    locations = Location.objects.filter(district_id=district_id).all()
    return render(request, 'officer/lcoation_list_options.htm', {'locations': locations})
    #return JsonResponse(list(cities.values('id', 'name')), safe=False)

  
  
#testing
def finelist(request):
    stud = Fine.objects.all()
    return render(request,'officer/officer_index.htm',{'stu': stud})