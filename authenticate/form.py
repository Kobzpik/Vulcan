from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Driver,Officer

class DriverSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

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
        driver.location=self.cleaned_data.get('location')
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
