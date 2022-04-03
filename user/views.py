from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def user_login(request):
    return render(request,'login.html')

def user_signup(request):
    return render(request,'signup.html')

def master(request):
    return render(request,'usermaster.html')
def view_hotels(request):
    return render(request,'hotels.html')
def profile(request):
    return render(request,'profile.html')
def view_resorts(request):
    return render(request,'resorts.html')    
