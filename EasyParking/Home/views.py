from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_view(request : HttpRequest):
    return render(request , "Base/Home.html")


def about(request : HttpRequest):
    return render(request , "Base/about.html")

