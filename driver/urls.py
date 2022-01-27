from django.urls import path
from .import views


urlpatterns = [
    path('driver_home/', views.index, name='driver_home'),
    path('fine_list/', views.fine_list, name='fine_list'),
   
    
    
]