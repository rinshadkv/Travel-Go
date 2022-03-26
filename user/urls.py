from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,),
    path ('signup/',views.signup),
    
    path('master/',views.master),
    path('hotels/',views.hotels),
    path('profile/',views.profile),
    path('resorts/',views.resorts),
    path('india_hotels/',views.india_hotels),
    path('middleeast_hotels/',views.middleeast_hotels),
    path('europe_hotels/',views.europe_hotels),
    path('others_hotels/',views.others_hotels),
    
    
    
    

    
    


]



