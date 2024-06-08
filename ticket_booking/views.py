from django.shortcuts import render, HttpResponseRedirect
from .models import FlightLocation, User, Booking
from django.contrib.auth import authenticate, login, logout



# paypalrestsdk.configure({
#     "mode": settings.PAYPAL_MODE,
#     "client_id": settings.PAYPAL_CLIENT_ID,
#     "client_secret": settings.PAYPAL_CLIENT_SECRET
    
#     })

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
        

        User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
                
                )
    return HttpResponseRedirect("/")
        
        

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
                
                login(req, user=user)
            return HttpResponseRedirect("/")
        except:
            pass

            return render("login.html")
       
    return render(req, "login.html")

def logout_view(req):
    logout(req)
    return HttpResponseRedirect("/")


def search_flight(req):
    if req.method == 'POST':
            
            return render(req, 'search_flight.html')
    else:
            form = FlightLocation()
            return render(req, "/")
def payment_page(req):
     return render(req, "payment.html")

# def create_payment(req):
#      if request.method == "POST":
#           payment = paypalrestsdk.Payment({
#                "intent": "sale",
#                "payer":{
#                     "payment_method":"paypal"
#                },
#                "redirect_urls":[
#                     "return_url":"http://localhost:8000/execute/",
#                     "cancle_urls": "http://localhost:8000/cancle/"
#                ],
#                "transactions":[{
#                     "item_list":{
#                          "items"
#                     }
#                }]
#           })








