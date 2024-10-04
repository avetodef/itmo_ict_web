from django import forms
from .models import Feedback

class Form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'last_name', 'age', 'email', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-class'}),
            'last_name': forms.TextInput(attrs={'class': 'input-class'}),
            'age': forms.TextInput(attrs={'class': 'input-class'}),
            'email': forms.TextInput(attrs={'class': 'input-class'}),
            'comment': forms.TextInput(attrs={'class': 'input-class'})
        }