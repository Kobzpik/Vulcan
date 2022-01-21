from django.urls import path
from .import views
from .views import userform

urlpatterns = [
    path('',views.index,name="index"),
    path('route/',userform,name="route"),
    

   
]