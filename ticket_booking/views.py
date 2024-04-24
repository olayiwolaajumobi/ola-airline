from django.shortcuts import render
from .models import FlightLocation

# Create your views here.

def index (req):

    location = FlightLocation.objects.all()

    return render(req, "index.html", {
        "location": location
    })


