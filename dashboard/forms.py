from django import forms
from .models import Impressions, Customers

class ImpressionForm(forms.ModelForm):
    class Meta:
        model = Impressions
        fields = ['name', 'star', 'impression', 'accept', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name...*'}),
            'star': forms.Select(choices=Impressions.picture_choice),
            'impression': forms.Textarea(attrs={'placeholder': 'Write here your personal impression about my services...*'}),
            'accept': forms.CheckboxInput(attrs={'required': 'required'}),
        }
        
class ImpressionForm1(forms.ModelForm):
    class Meta:
        model = Impressions
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'input-change'})
        }
        
class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'host_pwd', 'host_email', 'admin_username', 'admin_password', 'website', 'cost', 'income']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name...*', 'class': 'input-add'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email...*', 'class': 'input-add'}),
            'host_pwd': forms.TextInput(attrs={'placeholder': 'Pythonanywhere password...*', 'class': 'input-add'}),
            'host_email': forms.EmailInput(attrs={'placeholder': 'Pythonanywhere email...*', 'class': 'input-add'}),
            'admin_username': forms.TextInput(attrs={'placeholder': 'Admin email...*', 'class': 'input-add'}),
            'admin_password': forms.TextInput(attrs={'placeholder': 'Admin password...*', 'class': 'input-add'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website url...*', 'class': 'input-add'}),
            'cost': forms.NumberInput(attrs={'placeholder': 'All costs...*', 'class': 'input-add'}),
            'income': forms.NumberInput(attrs={'placeholder': 'All income...*', 'class': 'input-add'})
        }