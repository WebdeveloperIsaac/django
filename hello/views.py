from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,"hello/index.html")

def isaac(request):
    return HttpResponse("Hello Isaac Glad YOu are Here")    

def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.upper(),
    }) 

