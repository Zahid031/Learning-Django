from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *


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

def myimagepage2(request):
    return render(request,'image2.html')

def form(request):
    return render(request,'form.html')


def submitmyform(request):
    mydict1 = {
        "var1": request.GET.get('email', 'No email provided'),       # Safely get 'email' key
        "var2": request.GET.get('password', 'No password provided'), # Safely get 'password' key
        "method": request.method
    }
    return JsonResponse(mydict1)
def form2(request):
    
    if request.method == "POST":
        form=feedback(request.POST)
        if form.is_valid():
            tittle=request.POST["tittle"]
            subject=request.POST["subject"]

            mydict={
                "form":feedback()
            }
            if tittle!=tittle.upper():
                mydict["error"]=True
                mydict["errormsg"]="Tittle should be capital"
                return render(request,'form2.html',context=mydict)
            else:        
                mydict["success"]=True
                mydict["successmsg"]="Form is Submitted"
                return render(request,'form2.html',context=mydict)
        
        
     
    elif request.method == "GET":
        form = feedback()   
        mydict={
            "form": form,
        }
        return render(request,'form2.html',context=mydict)
def error_404_view(request,exception):
    return render(request,'404.html')