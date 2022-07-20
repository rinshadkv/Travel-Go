from email import message
from django.shortcuts import redirect, render
from user.models import*
from host.models import *

# Create your views here.
def admin_dashboard(request):
    
    return render(request,'admin-dashboard.html')

def view_users(request):
    user_data=User.objects.all()

    return render(request,"user.html",{"user":user_data})

def manage_host(request):
    host_data=Account.objects.filter(status="True")


    return render(request,"manage-host.html",{"host":host_data})

def view_bookings(request):
    return render(request,"view-bookings.html")    

def admin_login(request):
    # message=""
    if request.method=='POST':
        email=request.POST["email"]  
        password=request.POST["password"]    
        admin_email="abcd@gmail.com"
        admin_password="12345678"
        if(email==admin_email)and(password==admin_password):
            return redirect("admin-dashboard")
        else:
            print("error")    
                
               
     
           
    return render(request,"admin-login.html")        

def new_host(request):
    host_data=Account.objects.filter(status="False")

    return render(request,"add-host.html",{"data":host_data})

def approve_host(request):
    host_data=Account.objects.get(id=request.POST['p_id'])
    if 'approve' in request.POST:
        host_data.status=True
    if 'decline' in request.POST:
        host_data.status=False
    host_data.save()    
    return redirect("manage-host")


def remove_host(request):
    host_data=Account.objects.get(id=request.POST['p_id'])
   
    if 'remove' in request.POST:
        host_data.status=False
    host_data.save()    
    return redirect("manage-host")