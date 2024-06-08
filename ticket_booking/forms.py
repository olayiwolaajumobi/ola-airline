from django import forms
from .models import Booking


class FlightLocation(forms.Form):
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)

class Booking(forms.ModelForm):
    class Meta:
        model = Booking
        field = ['passanger_name', 'passanger_email' ]