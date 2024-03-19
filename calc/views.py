from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Sanjeev'} )

def add(request):

    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2

    return render(request,'result.html',{'result':res})

def sub(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res2=val1-val2
    return render(request,'result1.html',{'result1':res2})