from django.urls import path
from .import views


urlpatterns = [
    path('driver_home/', views.index, name='driver_home'),
    path('fine_list/<int:pk>/', views.fine_list, name='fine_list'),
   
    
    
]