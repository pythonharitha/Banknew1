
from django.contrib.auth.forms import UserCreationForm
from django import forms
from bankapp_new.models import District, Branch, Customer


class NewCreationForm(forms.ModelForm):
    class Meta:
     model= Customer
     fields= 'district','branch','Account_type'