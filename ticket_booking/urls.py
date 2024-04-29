from django.urls import path
from .views import index, create_account, login_view, logout_view


urlpatterns = [ 
    path("", index),
    path("create", create_account),
    path("login", login_view),
    path("logout", logout_view)
]

