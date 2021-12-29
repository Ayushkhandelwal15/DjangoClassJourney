from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        dests=place.objects.all()
        print('In Home')
        print(User.is_authenticated)
        return  render(request,'index.html',{'dests':dests})
    else:
        return render(request, 'login.html')
    #return  HttpResponse("Welcome to Django session")

def about(request):
    return  render(request,'about.html')











#Below code is when data is beging use with Database or migration
# def Home(request):
#     dest1=place()
#     dest1.city_name='Bangalre'
#     dest1.descri='noise'
#     dest1.price='3000'
#     dest1.image='destination_2.jpg'
#     dest1.offer=True
#
#     dest2 = place()
#     dest2.city_name = 'Bangalre'
#     dest2.descri = 'noise'
#     dest2.price = '3000'
#     dest2.image = 'destination_3.jpg'
#     dest2.offer = True
#
#     dest3 = place()
#     dest3.city_name = 'Pune'
#     dest3.descri = 'Nothing Good'
#     dest3.price = '200'
#     dest3.image = 'destination_5.jpg'
#     dest3.offer = True
#
#     dest4  = place()
#     dest4.city_name = 'Hyderbaad'
#     dest4.descri = 'Idly'
#     dest4.price = '4000'
#     dest4.image = 'destination_4.jpg'
#     dest4.offer = True
#
#     dests=[dest1,dest2,dest3]
#
#     return  render(request,'index.html',{'dests':dests})
#     #return  HttpResponse("Welcome to Django session")
