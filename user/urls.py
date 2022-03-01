from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login, name='login'),
    path ('signup/',views.signup),
    path('index/',views.index),
    path('master/',views.master),
    path('fivestar/',views.fivestar)


]



