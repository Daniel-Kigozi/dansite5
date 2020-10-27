from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [

            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save address'))
