from django import forms
from .models import Zakaz


class ZakazCreateForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = [
            'name',
            'email',
            'body_zakaz'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control rows=5'}),
            'email': forms.EmailInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'body_zakaz': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }

