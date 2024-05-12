from django import forms
from webapp.models import users

class Modelform(forms.ModelForm):
    class Meta:
        model=users
        fields='__all__'
        widget={
            'user_id': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }
