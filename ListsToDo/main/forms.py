from .models import List
from django.forms import ModelForm, TextInput, Textarea


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ["title", "list"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название списка'
            }),
            "list": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите список',
            }),
        }