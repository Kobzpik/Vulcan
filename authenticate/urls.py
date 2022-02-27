from django.urls import path
from .import views


urlpatterns = [
    path('home/', views.home, name='home'),
     path('profile_officer/',views.profile_officer, name='profile_officer'),
     path('profile_driver/',views.profile_driver, name='profile_driver'),
     path('driver_register/',views.driver_register.as_view(), name='driver_register'),
     path('officer_register/',views.officer_register.as_view(), name='officer_register'),
     #path('profile/', views.profile, name='profile'),
     path('login_driver/',views.login_requestDriver, name='login_driver'),
     path('login_police/',views.login_requestPolice, name='login_police'),
     path('logout/',views.logout_view, name='logout'),
     path('verify/',views.verify_view,name='verify'),
    
]