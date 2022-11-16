from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("signIn/" , views.signIn , name="signIn"),
    path("signUp/" , views.new_user , name="new_user"),
    path("all_places/" , views.all_places , name="all_places"),
    path("info_reserve/" , views.information_and_reserve , name="information_and_reserve"),
    path("logOut/" , views.logOut , name= "logOut"),
    path("add_place" , views.add_place , name="add_place"),
    path("manage/" , views.owner_manage , name="owner_manage")
   
   ]