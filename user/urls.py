from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.user_login,),
    path ('signup/',views.user_signup),
    path('master/',views.master),
    path('hotels/',views.view_hotels,name='hotels'),
    path('resorts/',views.view_resorts,name='resorts'),
    path('home/',views.home2 ,name='home2'),
    path('profile/',views.profile,name='profile'),
    path('view-hotel/<int:p_id>',views.view_hotel_details,name='hotels'),
    path('book-hotel/<int:r_id>',views.book_hotel,name='book-hotel'),
    path('change_details',views.change_details,name='change_details'),
    path('change_password',views.change_password,name='change_password'),
    path('search/',views.search_hotel,name='search'),
    path('log_out/',views.log_out,name='log_out'),
    path("check_avilable/",views.check_avilable),
    path("book_now/",views.book_details),
    
    path("check_email/",views.check_email),
    path("payment_at_hotel/",views.hotel_payment_hotel),
    path("payment_online/",views.online_payment)

    
    
   
    
    
    

    
    


]



