from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.host,name='host-mainpage'),
    path('host_signup/',views.host_signup,name="signup"),
    path('hotel-details/',views.hotel_details,name='hotel_details'),
    path('host-registration2/',views.host_registration_2),
    path('host-dashboard/',views.host_dashboard,name='dashboard'),
    path('host-view-booking/',views.view_booking), 
    path('add-room',views.add_room,name='add-room'),
    path('host-login/',views.host_login,name='login'),
    path('host-profile/',views.host_profile,name='host-profile'),
    path('guest-reviews/',views.guest_reviews),
    # path('add_property',views.add_property),
    path('update-details/',views.change_personaldetails,name='update-personal'),
    path('update-login-details/',views.change_logindetails),
    path('update-password/',views.update_password),
    path('update-profile-image/',views.update_profile_photo),
    path('host_log_out/',views.log_out,name='host_log_out'),
    path('update-room/',views.update_room_details),
    path('change-status/',views.change_status),
    path('upload_room_images/',views.upload_room_images),
    path('upload_hotel_images/',views.upload_hotel_images),
    path("add-amenities/",views.add_facility,),
    path("about-property/",views.about_hotel),
    path("check_details/",views.check_details),
    path("check_email/",views.check_email)



]