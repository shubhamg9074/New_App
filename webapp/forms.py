from django import forms
from webapp.models import Student

class Modelform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widget={
            'user_id': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_my_field(self):
        user_id = self.cleaned_data.get('user_id')
        if Student.objects.filter(user_id=user_id).exists():
            raise forms.ValidationError("This primary key is already taken.")
        return user_id