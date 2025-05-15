# myapp/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Type Your Messages', 'rows': 4}))

