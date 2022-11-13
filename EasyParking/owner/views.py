from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def signIn(request : HttpRequest):
    return render(request , "owner/signIn.html")


def new_owner(request : HttpRequest):
    return render(request , "owner/signUp.html")