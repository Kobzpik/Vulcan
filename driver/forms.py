from django import forms
from driver.models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'