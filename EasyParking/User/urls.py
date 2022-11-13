from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signIn/" , views.signIn , name="signIn"),
    path("signUp/" , views.new_user , name="new_user"),
    path("all_places/" , views.all_places , name="all_places"),
    path("info_reserve/" , views.information_and_reserve , name="information_and_reserve"),
    path("manage/<reserve_id>" , views.manage , name="manage")
]