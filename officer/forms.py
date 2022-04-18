from django import forms

from officer.models import Fine, Location,Accident


class FineCreationForm(forms.ModelForm):
    class Meta:
        model = Fine
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.all()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['location'].queryset = Location.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input ; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['location'].queryset = self.instance.district.location_set.order_by('name')
     


class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = '__all__'