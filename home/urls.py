from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home-home'),
    path('loggedin/',views.userhome,name="user-home")

]