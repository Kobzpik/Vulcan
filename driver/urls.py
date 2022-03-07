from django.urls import path
from .import views


urlpatterns = [
    path('driver_home/', views.index, name='driver_home'),
    path('fine_list/<int:pk>/', views.fine_list, name='fine_list'),
    path('payment/', views.home, name='payment'),
    path('payment/create-checkout-session/', views.create_checkout_session, name='checkout'),
    path('success/', views.success,name='success'),
    path('cancel/', views.cancel,name='cancel'),
    #path('webhooks/stripe/',views.webhook,name="webhook")

    
    
]