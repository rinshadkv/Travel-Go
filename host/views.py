from django.shortcuts import render

# Create your views here.
def host(request):
    return render(request,'host_view1.html')

def host_signup(request):
    return render(request,'host_signup.html')  

def host_dashboard(request):
    return render(request,'host-master.html') 

def hotel_details(request):
    return render(request,'hotel-details.html') 
  
def host_registration(request):
    return render(request,'host-reg.html') 

def host_registration_2(request):
    return render(request,'host-reg2.html')

def dashboard(request):
    return render(request,'host-dashboard.html') 


def view_booking(request):
    return render(request,'host-view-booking.html') 

def add_rooms(request):
    return render(request,'host-add-rooms.html') 

def host_login(request):
    return render(request,'host-login.html') 

def host_profile(request):
    return render(request,'host-profile.html') 
