from django import forms

from store.models import Vehicle
# from models import fuel_options,owner_options

class VehicleForm(forms.Form):

    name=forms.CharField()

    varient=forms.CharField()

    description=forms.CharField()

    fuel_type=forms.ChoiceField(choices=Vehicle.fuel_options)

    running_km=forms.IntegerField()

    color=forms.CharField()

    price=forms.IntegerField()

    brand=forms.CharField()

    owner_type=forms.ChoiceField(choices=Vehicle.owner_options)
