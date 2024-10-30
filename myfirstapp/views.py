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


def myfirstpage(request):
    return render(request,'index.html')
def mysecondpage(request):
    return render(request,'second.html')
def mythirdpage(request):
    var="Fruits"
    greetings="Hii,How are you?"
    fruits=["mango","banana","......"]
    a = 1
    b = 2
    ans = a>b
    print(ans)
    mydictionary={
        "var":var,
        "msg":greetings,
        "myfruits":fruits,
        "a" :a,
        "b" :b,
        "ans" :ans
    }
    return render(request,'third.html',context=mydictionary)
def myimagepage(request):
    return render(request,'image.html')