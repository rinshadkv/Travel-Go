from django.urls import path
from . import views

urlpatterns=[
    path('',views.admin_login,name='admin-login'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    
    path("manage-host/",views.manage_host,name="manage-host"),
    path("view-users/",views.view_users),
    path("view-booking/",views.view_bookings),
    path("add-host/",views.new_host),
    path("approve-host/",views.approve_host),
    path("remove-host/",views.remove_host)
    
    
    
    
    
    
    ]