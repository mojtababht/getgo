from .models import *
from django import forms


class RequestForm(forms.ModelForm):

    class Meta:
        model=Request
        fields=['type','sAddress','dAddress']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['lat','long']


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

