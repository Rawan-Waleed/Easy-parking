from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from Home.models import Add_Place , User_Reservation 



# Create your views here.

def signIn(request : HttpRequest):
    message = ""
    if request.method == "POST":
        user = authenticate(request , username = request.POST["email"] , password=request.POST["password"])
        if user:
            login(request,user)
            return redirect ("users:all_places")
        else:
            message = "Not Fount , please entre correct email or password"

    return render(request , "user/user_signIn.html" , {"message" : message})


def new_user(request : HttpRequest):
    if request.method == "POST":
      user = User.objects.create_user(username = request.POST["email"] , email = request.POST["email"] , first_name = request.POST["first_name"], last_name = request.POST["last_name"] , password=request.POST["password"])
      user.save()
    
      profile = Profile(user=user, phone_number = request.POST["phone_number"] , is_owner = request.POST["is_owner"])
      profile.save()
    return render(request , "user/user_signUp.html")


def logOut(request : HttpRequest):
    logout(request)
    return redirect("Home:Home")


def all_places(request : HttpRequest):
    places = Add_Place.objects.all()
    
    return render(request , "user/all_places.html" , {"place" : places})


def information_and_reserve(request : HttpRequest , reserve_id :int):
    if request.method == "POST":
      user_reserve = User_Reservation(user = request.user, parking_reserve= request.POST["parking_reserve"] , hours = request.POST["hours"] , day = request.POST["day"], start_time = request.POST["start_time"] , end_time =request.POST["end_time"])
      user_reserve.save()
      return redirect ("users:success_resservation" , user_reserve)

    information = Add_Place.objects.all()
    return render(request , "user/information_and_reserve.html" , {"place_info" :information })


def user_reserve_information(request : HttpRequest  , reserve_id: int): 

     if request.method == "POST":
      user_reserve = User_Reservation(user = request.user, parking_reserve= request.POST["parking_reserve"] , hours = request.POST["hours"] , day = request.POST["day"], start_time = request.POST["start_time"] , end_time =request.POST["end_time"])
      user_reserve.save()
      return redirect ("users:success_resservation" , {"success" , user_reserve})

     return render(request , "user/information_and_reserve.html" )



def add_place(request : HttpRequest):

    if request.method == "POST":
      place_add = Add_Place(user = request.user, place_name= request.POST["place_name"] , address = request.POST["address"] , Price = request.POST["Price"], number_parking = request.POST["number_parking"] , days =request.POST["days"], open_time =request.POST["open_time"], close_time =request.POST["close_time"])
      place_add.save()
      return redirect ("users:all_places")

    return render(request , "user/add_place.html" )
    

def owner_manage(request : HttpRequest):
    all_reservation = User_Reservation.objects.all()
    all_reservation2 = Profile.objects.all()
    return render(request , "user/owner_manage.html" , {"users_reservation": all_reservation , "users_reservation2" : all_reservation2})



def success_resservation(request : HttpRequest, reserve_id :int):
    user2_reserve = User_Reservation.objects.all()
    return render(request , "user/success_reservation.html"  , {"success1":user2_reserve})


def delete_reservation(request : HttpRequest , reserve_id:int):
    reserve = User_Reservation.objects.get(id = reserve_id)
    reserve.delete()
    return redirect("users:manage")


def user_reserve_manage(request : HttpRequest , reserve_id : int):
    return render(request , "user/manage_reserve.html")