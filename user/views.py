from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
def master(request):
    return render(request,'usermaster.html')
def hotels(request):
    return render(request,'hotels.html')
def profile(request):
    return render(request,'profile.html')
def resorts(request):
    return render(request,'resorts.html')    
def middleeast_hotels(request):
    return render(request,'middleeast-hotels.html')        
def india_hotels(request):
    return render(request,'india-hotel.html')    
def europe_hotels(request):
    return render(request,'europe-hotels.html')            
def others_hotels(request):
    return render(request,'others-hotels.html')                
                   