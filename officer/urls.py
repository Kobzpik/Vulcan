from django.urls import path
from .import views


urlpatterns = [
     path('fine_add/', views.fine_create_view, name='fine_add'),
    path('<int:pk>/', views.fine_update_view, name='fine_change'),
    path('ajax/load-locations/', views.load_locations, name='ajax_load_locations'), # AJAX
    
    
]