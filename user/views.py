from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
def index(request):
    return render(request,'index.html')
def master(request):
    return render(request,'usermaster.html')
def fivestar(request):
    return render(request,'5 star.html')