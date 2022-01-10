from django.urls import path
from .import views
from django.contrib.auth import views as auth_view




urlpatterns = [
    path('', views.home, name='home'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='authenticate/login.htm'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='authenticate/logout.htm'), name="logout"),
    
]