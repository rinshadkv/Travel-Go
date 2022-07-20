from email import message
import email
from multiprocessing import context
from pickle import TRUE
from pyexpat.errors import messages
from socket import MsgFlag
from tabnanny import check
from tkinter import Place
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render
import json
import random

from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.


def host(request):

    return render(request, 'host_view1.html')


def host_signup(request):
    json_data = open('/Travel go/country.json')
    data1 = json.load(json_data)  # deserialises it
    data2 = json.dumps(data1)  # json formatted string

    json_data.close()
    if request.method == 'POST':
        name = request.POST['name']
        country = request.POST['country']
        countrycode = request.POST['countrycode']
        phone = request.POST['phone']
        place = request.POST['place']
        type = request.POST['property_type']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES['pic']
        obj = Property(property_name=name, country=country, countrycode=countrycode, phone=phone,
                       place=place, property_type=type, image=image)
        obj.save()
        data = Property.objects.get(id=obj.id)
        account = Account(email=email, password=password, property_id=data)
        account.save()
        return redirect('login')

    else:

        return render(request, 'host_signup.html', {'data': data1})

def check_details(request):
   
    name=request.GET['name']
   
    countrycode = request.GET['countrycode']
    phone = request.GET['phone']
    
    

    data2=Property.objects.filter(property_name=name,countrycode=countrycode,phone=phone).exists()
    

    return JsonResponse({"property_exists":data2})


    
def check_email(request):
    email=request.GET["email"]
    data=Account.objects.filter(email=email).exists()
    return JsonResponse({"exists":data})


def hotel_details(request):
    
    room_data = Rooms.objects.filter(property_id=request.session['hotel_id'])
    hotel_data=Property.objects.get(id=request.session['hotel_id'])
    hotel_images=property_images.objects.filter(property_id=request.session['hotel_id'],type='hotel')
    room_images=property_images.objects.filter(property_id=request.session['hotel_id'],type='rooms')
    hotel_desc=AboutProperty.objects.filter(property_id=request.session['hotel_id'])
    amenities=AddAmenities.objects.filter(property_id=request.session['hotel_id'])
    
   
    context={
    'data':room_data,
    'data2':hotel_data,
    'hotel':hotel_images,
    'rooms':room_images,
    'desc':hotel_desc,
    'amenities':amenities

    }
    print(hotel_desc)
    
    return render(request, 'hotel-details.html',context)

def change_status(request):
    room_data=Rooms.objects.get(id=request.POST['r_id'])
    if 'avilable' in request.POST:
        room_data.status=True
    if 'unavilable' in request.POST:
        room_data.status=False
    room_data.save()
    return redirect('hotel_details')


def host_registration_2(request):
    return render(request, 'host-reg2.html')


def host_dashboard(request):

    return render(request, 'host-dashboard.html')


def view_booking(request):
    return render(request, 'host-view-booking.html')


def add_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        room_number=request.POST['room_number']
        adult = request.POST['adult']
        child = request.POST['child']
        price = request.POST['price']
        beds = request.POST['beds']
        hotel_id = Property.objects.get(id=request.session['hotel_id'])

        obj = Rooms(room_name=room_name, adult=adult, child=child,
                    price=price, beds=beds, property_id=hotel_id,room_number=room_number)
        obj.save()
        message = 'romm added successfully'
        return render(request,'host-add-rooms.html',{'msg':message})
    else:

        return render(request, 'host-add-rooms.html')




def update_room_details(request):
    if request.method=='POST':
        room_id=request.POST['room_id']
        room_name=request.POST['room_name']
        adult=request.POST['adult']
        child=request.POST['child']
        price=request.POST['price']
        beds=request.POST['beds']
        room_data=Rooms.objects.get(id=room_id)
        room_data.room_name=room_name
        room_data.adult=adult
        room_data.child=child
        room_data.price=price
        room_data.beds=beds
        room_data.save()

    return redirect('hotel_details')

def upload_room_images(request):
    
    room_images=request.FILES['room_images']
   
    
    type='rooms'
    hotel_id = Property.objects.get(id=request.session['hotel_id'])
    obj=property_images(property_image=room_images,type=type,property_id=hotel_id)
    obj.save()
    return redirect('hotel_details')
    
    

def upload_hotel_images(request):
    print('hiii')
   
    hotel_images=request.FILES['hotel_images']
    type='hotel'
    hotel_id = Property.objects.get(id=request.session['hotel_id'])
    obj=property_images(property_image=hotel_images,type=type,property_id=hotel_id)
    obj.save()
    return redirect('hotel_details')



def host_login(request):
    message = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            data = Account.objects.get(email=email, password=password)
            request.session['hotel_id'] = data.property_id.id
            return redirect("dashboard")
        except:
            message = "Username or password incorrect"

    return render(request, 'host-login.html', {'errmsg': message})


def change_personaldetails(request):

    name = request.GET['name']
    country = request.GET['country']
    phone = request.GET['phone']
    list1 = phone.split()
    country_code = list1[0]
    phone_number = int(list1[1])
    Place = request.GET['place']
    host_data = Property.objects.get(id=request.session['hotel_id'])
    host_data.property_name = name
    host_data.country = country
    host_data.countrycode = country_code
    host_data.phone = phone_number
    host_data.place = Place
    host_data.save()

    message = True

    return JsonResponse({'msg': message})


def change_logindetails(request):

    try:

        email = request.GET['email']
        host_data = Account.objects.get(
            property_id=request.session['hotel_id'])

        host_data.email = email
        host_data.save()
        message = True

    except:
        message = False
    return JsonResponse({'msg': message})


def update_profile_photo(request):

    new_photo = request.FILES['file']

    host_data = Property.objects.get(id=request.session['hotel_id'])

    host_data.image = new_photo
    host_data.save()

    return JsonResponse({'msg': 'updated', 'img': host_data.image.url})


def update_password(request):

    try:
        old_password = request.GET['old_password']
        new_password = request.GET['new_password']
    
        host_data = Account.objects.get(
            property_id=request.session['hotel_id'])

        if host_data.password == old_password:
            host_data.password = new_password
            host_data.save()
            message = True

       
        else:
            message = False
    except:
           pass

    return JsonResponse({'msg': message})


def host_profile(request):
    hotel_data = Account.objects.get(property_id=request.session['hotel_id'])

    return render(request, 'host-profile.html', {'data': hotel_data})


def guest_reviews(request):
    return render(request, 'guest-reviews.html')

def log_out(request):
    del request.session['hotel_id']
    request.session.flush()

    return redirect('login')

def remove_room(request):
    return redirect("")

def add_facility(request):
    if request.method=="POST":
        amenities=request.POST['amenities']
        hotel_id = Property.objects.get(id=request.session['hotel_id'])
        obj=AddAmenities(amenities=amenities,property_id=hotel_id)
        obj.save()
        return redirect("hotel_details")
    else:
        pass
    return render(request,"hotel-details.html")    



def about_hotel(request):
    if request.method=="POST":
        description=request.POST['description']
        rules=request.POST['rules']
        hotel_id = Property.objects.get(id=request.session['hotel_id'])
        obj=AboutProperty(description=description,rules=rules,property_id=hotel_id)
        obj.save()
        return redirect("hotel_details")
    else:
        pass
    return render(request,"hotel-details.html")    









   