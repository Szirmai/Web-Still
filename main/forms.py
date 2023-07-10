from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Basic(forms.ModelForm):
    class Meta:
        model = models.Offer  # Use the renamed variable
        fields = ['pack1', 'pack2', 'pack3', 'pack4', 'pack6', 'pack7', 'pack8', 'pack9', 'pack10', 'pack11', 'pack12', 'SpecialWish', 'accept', 'name', 'email', 'SpecialWish', 'WebsiteType', 'goal', 'aboutproject', 'extra', 'accept']
        labels = {}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '* Your name...'}),
            'email': forms.EmailInput(attrs={'placeholder': '* Your Email...'}),
            'pack1': forms.Select(attrs={'class': 'select'}),
            'pack2': forms.Select(attrs={'class': 'select'}),
            'pack3': forms.Select(attrs={'class': 'select'}),
            'pack4': forms.Select(attrs={'class': 'select'}),
            'pack6': forms.Select(attrs={'class': 'select'}),
            'pack7': forms.Select(attrs={'class': 'select'}),
            'pack8': forms.Select(attrs={'class': 'select'}),
            'pack9': forms.Select(attrs={'class': 'select'}),
            'pack10': forms.Select(attrs={'class': 'select'}),
            'pack11': forms.Select(attrs={'class': 'select'}),
            'pack12': forms.Select(attrs={'class': 'select'}),
            'SpecialWish': forms.Textarea(attrs={'class': 'wish-text-area', 'placeholder': 'Write here your extra wishes...'}),
            'WebsiteType': forms.Select(attrs={'class': 'select'}),
            'aboutproject': forms.Textarea(attrs={'class': 'wish-text-area', 'placeholder': 'What purpose does it serve? When should it be ready? Write a little about design or about the basic concept of the website...'}),
            'goal': forms.Select(attrs={'class': 'select'}),
            'extra': forms.Textarea(attrs={'class': 'wish-text-area', 'placeholder': 'Something we haven\'t talked about yet? It\'s your time...'}),
            'accept': forms.CheckboxInput(attrs={'required': 'required'}),
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'phone', 'email', 'subject', 'message', 'accept']
        labels = {}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '* Your name...'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Phone numer... (opional)'}),
            'email': forms.EmailInput(attrs={'placeholder': '* Your E-mail...'}),
            'subject': forms.TextInput(attrs={'placeholder': '* Subject...'}),
            'message': forms.Textarea(attrs={'class': 'wish-text-area', 'placeholder': '* Your message...'}),
            'accept': forms.CheckboxInput(attrs={'required': 'required'}),
        }