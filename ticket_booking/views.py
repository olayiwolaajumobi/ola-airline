from django.shortcuts import render, HttpResponseRedirect
from .models import FlightLocation
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index (req):

    location = FlightLocation.objects.all()

    return render(req, "index.html", {
        "location": location
    })
def create_account(req):
    if req.method == "POST":
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        

        try:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
                
                )
            return HttpResponseRedirect("/")
        except:
            print("error")
            pass

    return render(req, "create_account.html")


def login_view(req):

    if req.method == "POST":
        username=req.POST["username"]
        password=req.POST["password"]

        try:
            user= authenticate(username=username, password=password)

            if user == None:
                return render(req, "login.html"), {
                    'error' : "wrong username or password"
                }
            else:
                
                login(req, user)
                try:
                    return HttpResponseRedirect(req.GET["next"])
                except:
                    return HttpResponseRedirect("/")
        except:
            pass

    return render(req, "login.html")

def logout_view(req):
    logout(req)
    return HttpResponseRedirect("/")







