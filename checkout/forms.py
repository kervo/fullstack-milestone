from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
                'full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'postcode': 'Post Code',
            'town_or_city': 'Town / City',
            'street_address1': 'Address 1',
            'street_address2': 'Address 2',
            'county': 'County/Region',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'  # Required
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
