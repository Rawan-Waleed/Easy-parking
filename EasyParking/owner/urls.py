from django.urls import path
from . import views

app_name = "owner"

urlpatterns = [

    path("signIn", views.signIn , name="signIn"),
    path("signUp/", views.new_owner , name="new_owner")
    
]