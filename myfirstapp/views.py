from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello Worlds!")

def myfunctionabout(request):
    return HttpResponse("This is about section")

def add(request,a,b):
    return HttpResponse(a+b)
def intro(request,name,age):
    dict1={
        "name":name,
        "age":age
    }
    return JsonResponse(dict1)