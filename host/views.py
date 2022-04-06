from django.shortcuts import render

# Create your views here.
def host(request):
    return render(request,'host_view1.html')

def host_signup(request):
    return render(request,'host_signup.html')  

def host_dashboard(request):
    return render(request,'host_dashboard.html')      