from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.user_login,),
    path ('signup/',views.user_signup),
    
    path('master/',views.master),
    path('hotels/',views.view_hotels),
    path('profile/',views.profile),
    path('resorts/',views.view_resorts),
   
    
    
    

    
    


]



