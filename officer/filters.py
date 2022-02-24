import django_filters
from django_filters import DateFilter

from .models import *

class Fine_filter(django_filters.FilterSet):

	

	class Meta:
		model = Fine
		fields = '__all__'
		exclude = ['id','vehicle_No','time','Police_station','Issuing_officer_Name','location','Nature_of_Offence','user_id','district','date']