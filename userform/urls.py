from django.urls import path

from . import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login_user,name="login"),
    path("search",views.Search,name="Search"),
    path("RoomType",views.RoomInfo, name="Roominfo"),
    path("HotelPnrDisplay",views.booking,name="booking"),
    path("roomcheck",views.reserve,name="reserve")

]