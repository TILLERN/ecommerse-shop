from django import forms


class checkout_form(forms.Form):
    
    first_name = forms.CharField(
        required=True,
        )
    last_name = forms.CharField(
        required=True,
        )
    email = forms.EmailField(
        required=True,
        )
    phone_number = forms.CharField(
        required=True,
        initial='+254'
        )
    CHOICES=[
        ('CBD_pickup','CBD_pickup'),
        ('custom_address','custom_address'),
        ]
    delivery_address = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
        )    
    city_or_town = forms.CharField(
        required=False,
        )
    estate = forms.CharField(
        required=False,
        )
    street = forms.CharField(
        required=False,
        )
    building = forms.CharField(
        required=False,
        )
    additional_information = forms.CharField(
        required=False,
        widget=forms.Textarea
        )