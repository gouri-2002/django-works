
from django import forms

from crm.models import Cars

class CarsForm(forms.Form):

    brand=forms.CharField()

    varient=forms.CharField()
    
    fuel_type=forms.ChoiceField(choices=Cars.fuel_options)

    transmission_type=forms.ChoiceField(choices=Cars.transmission_options)

    color=forms.CharField()

    price=forms.IntegerField()

    mileage=forms.IntegerField()

    
    
    
