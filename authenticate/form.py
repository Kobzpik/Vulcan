from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Driver,Officer,Codes

class DriverSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    driver_license_No = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        driver = Driver.objects.create(user=user)
        driver.phone_number=self.cleaned_data.get('phone_number')
        driver.driver_license_No=self.cleaned_data.get('driver_license_No')
        driver.save()
        return user

class OfficerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_officer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        officer = Officer.objects.create(user=user)
        officer.phone_number=self.cleaned_data.get('phone_number')
        officer.designation=self.cleaned_data.get('designation')
        officer.save()
        return user

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Codes', help_text='Enter varification code')
    class Meta:
        model = Codes
        fields = ['number']