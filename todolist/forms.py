from django import forms
from .models import Todolist

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['title', 'description',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'label': 'kl'}),
            'description': forms.Textarea(attrs={'class': 'form-control fixed-width ', 'rows': 4, 'placeholder': 'Enter description'}),
        }
        labels = {
            'title': '',  # Set label to an empty string
            'description': '',  # Set label to an empty string
        }
        
        