from django.urls import path
from .import views


urlpatterns = [
    path('driver_home/', views.index, name='driver_home'),
   
    
    
]