from django import forms
from .models import Product

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    product = forms.ModelChoiceField(queryset=Product.objects.exclude(category=8), empty_label="Select one...")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your message...'}))
