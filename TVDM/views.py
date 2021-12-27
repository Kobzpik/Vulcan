from django.shortcuts import render

# Create your views here.
def home(request):
        return render(request, 'index.htm')


def testRoute(request):
        return render(request, 'route.htm')