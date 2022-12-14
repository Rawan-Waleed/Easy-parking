from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("signIn/" , views.signIn , name="signIn"),
    path("signUp/" , views.new_user , name="new_user"),
    path("all_places/" , views.all_places , name="all_places"),
    path("info_reserve/<reserve_id>/" , views.information_and_reserve , name="information_and_reserve"),
    path("user_reserve/<reserve_id>" , views.user_reserve_information , name="user_reserve_information"),
    path("logOut/" , views.logOut , name= "logOut"),
    path("add_place" , views.add_place , name="add_place"),
    path("manage/" , views.owner_manage , name="owner_manage"),
    path("success/<reserve_id>/" , views.success_resservation , name="success_resservation"),
    path("delete/<reserve_id>/" , views.delete_reservation , name="delete_reservation")
   
   ]