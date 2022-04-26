from django.urls import path
from . import views

urlpatterns=[
    path('',views.host,name='host-mainpage'),
    path('host_signup/',views.host_signup,name="signup"),
    path('host_dashboard/',views.host_dashboard),
    path('hotel-details/',views.hotel_details),
    path('host-registration/',views.host_registration),
    path('host-registration2/',views.host_registration_2),
    path('host-dashboard/',views.dashboard),
    path('host-view-booking/',views.view_booking),
    path('host-add-rooms/',views.add_rooms),
    path('host-login/',views.host_login),
    path('host-profile/',views.host_profile),

]