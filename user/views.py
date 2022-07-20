import email
from email import message
from multiprocessing import context
from operator import truediv
from pickle import OBJ
import re
from statistics import mode
from tkinter import ROUND, Place
from turtle import title
from wsgiref.handlers import read_environ
from django.shortcuts import render,redirect
from host.views import hotel_details

import user
from .models import *
from user.models import User
import json
import razorpay
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from host.models import *
from django.db.models import Q

# from user.models import User

# Create your views here.
def home(request):
    user_data=''
    if 'user_id' in request.session:
        try:
            user_data=User.objects.get(id=request.session['user_id'])
        except:
            pass    
    return render(request,'index.html',{'user':user_data})

def user_login(request):
    msg=''
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
       
        try:
            data=User.objects.get(email=email,password=password)
            request.session['user_id']=data.id
            return redirect("home2")
        except:
            msg="Username or password incorrect"
    
        
    return render(request,'login.html',{'err_msg':msg,})

def user_signup(request):
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        obj=User(email=email,password=password,name=name)   
        obj.save()
        request.session['user_id']=obj.id
        return redirect('home2')
    else:    

      return render(request,'signup.html')

def check_email(request):
    email=request.GET['email']
    data=User.objects.filter(email=email).exists()
    return JsonResponse({"exists":data})

def master(request):
    return render(request,'usermaster.html')

def view_hotels(request):
    property_details=[]
    property_dict={}
    img_key="img"
    show_resorts=Account.objects.filter(property_id_id__property_type="hotel",status="True")

    for hotels in show_resorts:

        property_dict={
            'property_name':hotels.property_id.property_name,
            'p_id':hotels.property_id.id,
            'place' : hotels.property_id.place,
            'country' : hotels.property_id.country,
            'prop_image':hotels.property_id.image,
        }
        property_details.append(property_dict)

        data = property_images.objects.filter(property_id=hotels.id)[:2]
        i=0
        for d in data:
            key=img_key+str(i)
            property_dict[key] = d.property_image
            i+=1
   


    return render(request,'hotels.html',{'h_data':property_details})

def profile2(request):
    return render(request,'profile2.html')

def profile(request):
    singledata=User.objects.get(id=request.session['user_id'])
   
    return render(request,'profile.html',{'data':singledata})
    
def view_resorts(request):
    property_details=[]
    property_dict={}
    img_key="img"
    show_resorts=Account.objects.filter(property_id_id__property_type="resort",status="True")

    for resorts in show_resorts:

        property_dict={
        'property_name':resorts.property_id.property_name,
        'p_id':resorts.property_id.id,
        'place' : resorts.property_id.place,
        'country' : resorts.property_id.country,
        'prop_image':resorts.property_id.image,
        }

        property_details.append(property_dict)



        data = property_images.objects.filter(property_id=resorts.id)[:2]
        i=0
        for d in data:
            key=img_key+str(i)
            property_dict[key] = d.property_image
            i+=1
    return render(request,'resorts.html',{'r_data':property_details})    
   
def home2(request):
    return render(request,'home.html')    

def view_hotel_details(request,p_id):
    hotel_details=Property.objects.get(id=p_id)
    hotel_images=property_images.objects.filter(property_id_id=p_id,type='hotel')
    room_image=property_images.objects.filter(property_id_id=p_id,type='rooms')
    room_details=Rooms.objects.filter(property_id_id=p_id,status='False')
    descriptions=AboutProperty.objects.filter(property_id=p_id)
    amenities=AddAmenities.objects.filter(property_id=p_id)
    print(descriptions)
    context={
        'h_data':hotel_details,
        'h_image':hotel_images,
        'r_data':room_details,
        'r_image':room_image,
        'desc':descriptions,
        "amenities":amenities


    }

    
    
    return render(request,'view-hotel.html',context)    

def book_hotel(request,r_id):
   
   
    room_details=Rooms.objects.get(id=r_id)
    user_data=User.objects.get(id=request.session['user_id'])
   

    return render(request,'book-hotel.html',{'data':room_details,'user':user_data} )



def change_password(request):
    
  
    old_password=request.GET['old_password']
    new_pass=request.GET['new_passwd']
    
    user_data=User.objects.get(id=request.session['user_id'])
    if  user_data.password==old_password:
        
            user_data.password=new_pass
            user_data.save()
             
            
            return JsonResponse({'status':True})
    return JsonResponse({'status':False})
     


def change_details(request):
    message=''
    if request.method=='POST':

        new_email=request.POST['email']
        new_name=request.POST['name']
        user_data=User.objects.get(id=request.session['user_id'])
        user_data.email=new_email
        user_data.name=new_name
        user_data.save()
        message='email and name updated successfully'
    return redirect('profile/',{'errmsg':message})
   

def search_hotel(request):
    property_details=[]
    property_dict={}
    img_key="img"
    if request.method=="POST":
        search_word=request.POST['search_box']
        search_list=search_word.split(' ')
      
        print(search_list)
        search_hotels=Account.objects.filter(Q(property_id_id__property_name__icontains=search_word)|
        Q(property_id_id__country__icontains=search_word)|Q(property_id_id__place__icontains=search_word),status="True")

        print(search_hotels)
        for property in search_hotels:
            property_dict= {}
            property_dict['property_name']=property.property_name
            property_dict['p_id']=property.id
            property_dict['place'] = property.place
            property_dict['country'] = property.country
            property_dict['prop_image']=property.image
            property_details.append(property_dict)
            data = property_images.objects.filter(property_id=property.id)[:2]
            i=0
            for d in data:
                key=img_key+str(i)
                print(key)
                property_dict[key] = d.property_image
                
                i+=1
        return render(request,'search.html',{'properties':property_details})    
        

    else:
        return redirect('home')    

def log_out(request):
    del request.session['user_id']
    request.session.flush()

    return redirect('home')
def check_avilable(request):
    check_in=request.GET["check_in"]
    room_id=request.GET["room_id"]
    print(check_in)

    date_avilble=Booking.objects.filter(check_in=check_in,room_id_id=room_id).exists()
    
   

    return JsonResponse({'isAvailable': date_avilble})

def book_details(request):
   

    check_in=request.POST['check_in']
    check_out=request.POST["check_out"]
    email=request.POST["email"]
    username=request.POST['username']
    user_id=request.POST["user_id"]
    room_id=request.POST["room_id"]
    
    return JsonResponse({"msg":True})
    
    # if(Payment_mode=="online"):
    #     Payment_mode="online payment"
       
    # else:
    #     Payment_mode="pay at hotel"   
    #      


        
        
        
        


@csrf_exempt
def hotel_payment_hotel(request):
        check_in=request.POST['check_in']
        # check_out=request.POST["check_out"]
        # email=request.POST["email"]
        # username=request.POST['username']
        # user_id=request.POST["user_id"]
        # room_id=request.POST["room_id"]
        obj=Booking(check_in=check_in,check_out=check_out,email=email,name=username,user_id_id=user_id,room_id_id=room_id)
        obj.save()

        request.session['booking_id']=obj.id
        price=request.POST["price"]
        payment_mode=request.POST["payment_mode"]
        payment_status=request.POST['payment_status']
        booking_data=Booking.objects.get(id=request.session['booking_id'])
        amount=Payment(price=price,payment_mode=payment_mode,booking_id=booking_data,payment_staus=payment_status)
        amount.save()
        return JsonResponse({"message":True})
        
@csrf_exempt
def online_payment(request):
    check_in=request.POST['check_in']
    check_out=request.POST["check_out"]
    email=request.POST["email"]
    username=request.POST['username']
    user_id=request.POST["user_id"]
    room_id=request.POST["room_id"]


    obj=Booking(check_in=check_in,check_out=check_out,email=email,name=username,user_id_id=user_id,room_id_id=room_id)
    obj.save()
    request.session['booking_id']=obj.id

    price=request.POST["price"]
    payment_mode=request.POST["payment_mode"]
    payment_status=request.POST['payment_status']
    booking_data=Booking.objects.get(id=request.session['booking_id'])

    
    amount=Payment(price=price,payment_mode=payment_mode,booking_id=booking_data,payment_staus=payment_status)
    amount.save()
    
    
    order_currency = 'INR'
    type(price)
    client = razorpay.Client(auth=('rzp_test_bOk1ozQycRBPsj','aUBvGPrWNowRFoRAjvkvoo1d'))
    payment = client.order.create({"amount": price, "currency": order_currency})
    return JsonResponse(payment)              