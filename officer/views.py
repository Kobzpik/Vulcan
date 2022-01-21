from django.shortcuts import render

# Create your views here.
def officer_index(request):
    return render(request, 'officer/officer_index.htm')