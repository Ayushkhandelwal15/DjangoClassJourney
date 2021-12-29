# from django.shortcuts import render
# from django.http import HttpRequest
#
# # Create your views here.
# def home(request):
#     return render(request,'home.html',{'course_name':'java'})
#



from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    #return  render(request,'hello.html')
    return  HttpResponse("Welcome to Django session")


def add(request):

    a= int(request.POST['number1'])
    b=int(request.POST['number2'])
    c=a+b
    return  render(request,'res.html',{'result':c})

def PersonalDetails(request):

    return render(request,'PersonalDetails.html')

def showDetails(request):

    Fname= request.POST['First Name']
    Lname= request.POST['Last Name']
    gender=request.POST['gender']

    return  render(request,'showDetails.html',{'showDetails':"Welcome" + Fname + " " +gender })
