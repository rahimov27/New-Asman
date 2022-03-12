from dataclasses import field
from telnetlib import Telnet
from . import models
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'phone', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", "placeholder": "Name"}),
            'phone': forms.TextInput(attrs={'class': "form-control", "placeholder": 'Phone'}),
            'email': forms.EmailInput(attrs={'class': "form-control", "placeholder": 'Email'}),
            'message': forms.TextInput(attrs={'class': "form-control", "placeholder": 'Message'}),
        }
