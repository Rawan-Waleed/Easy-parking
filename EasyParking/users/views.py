from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def signIn(request : HttpRequest):
    message = ""
    if request.method == "post":
        user = authenticate(request , email = request.POST["email"] , password=request.POST["password"])
        if user:
            login(request,user)
            return redirect ("users:all_places")
        else:
            message = "Not Fount , please entre correct email or password"

    return render(request , "user/user_signIn.html" , {"message" : message})


def new_user(request : HttpRequest):
    if request.method == "POST":
     user = User.objects.create_user(username= request.POST["email"] , email = request.POST["email"] , first_name = request.POST["first_name"], last_name = request.POST["last_name"] , password=request.POST["password"])
     user.save()
    
     profile = Profile(user=user, phone_number = request.POST["phone_number"])
     profile.save()

     return redirect ("users:all_places")

    return render(request , "user/user_signUp.html")


def logOut(request : HttpRequest):
    logout(request)
    return redirect("Home:Home")


def all_places(request : HttpRequest):
    return render(request , "user/all_places.html")

def information_and_reserve(request : HttpRequest):
    return render(request , "user/information_and_reserve.html")


def user_reserve_manage(request : HttpRequest , reserve_id : int):
    return render(request , "user/manage_reserve.html")

def user_reserve_information(request : HttpRequest ):
    return render(request , "user/reserve_info.html")


def add_place(request : HttpRequest):
    return render(request , "user/add_place.html")
    

def owner_manage(request : HttpRequest):
    return render(request , "user/owner_manage.html")