from django.urls import path
from . import views

urlpatterns=[
    path('',views.host),
    path('host_signup/',views.host_signup),
    path('host_dashboard/',views.host_dashboard),
]