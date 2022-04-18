from django.urls import path
from .import views


urlpatterns = [
    path('fine_add/', views.fine_create_view, name='fine_add'),
    # path('fine_add/', views.finelist, name='fine_add'),
    path('fine_change/<int:pk>/', views.fine_update_view, name='fine_change'),
    path('ajax/load_locations/', views.load_locations, name='ajax_load_locations'), # AJAX
    path('offence_details/', views.offenceDetails, name='offence_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('driver_info/', views.driver_info, name='driver_info'),
    path('accident/', views.accident, name='accident'),
                                                          
    
    
]