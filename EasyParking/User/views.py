from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def signIn(request : HttpRequest):
    return render(request , "user/signIn.html")


def new_user(request : HttpRequest):
    return render(request , "user/signUp.html")


def all_places(request : HttpRequest):
    return render(request , "user/all_places.html")

def information_and_reserve(request : HttpRequest):
    return render(request , "user/information_and_reserve.html")


def manage(request : HttpRequest , reserve_id : int):
    return render(request , "user/manage.html")

def reserve_information(request : HttpRequest ):
    return render(request , "user/reserve_info.html")