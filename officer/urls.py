from django.urls import path
from .import views


urlpatterns = [
    path('officer_index/', views.officer_index, name='officer_index'),
    
    
]