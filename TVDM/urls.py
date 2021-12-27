from django.urls import path
from .import views
from .views import testRoute

urlpatterns = [
    path('',views.home,name="home"),
    path('route/',testRoute,name="route"),

   
]