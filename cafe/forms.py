from django import forms
from cafe.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['your_name', 'your_email', 'your_phone', 'message']