from django.urls import path
from .import views
from .views import userform

urlpatterns = [
    path('',views.home,name="home"),
    path('route/',userform,name="route"),
    

   
]