from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def sample(request):
    return HttpResponse('Hello World')

def sample1(request):
    return HttpResponse('welcom to django')

def sampleInfo(request):
    # data={'name':'sravani','age':21,'city':'Hyderabad'}
    data={'result':[6,16,18,19]}
    return JsonResponse(data,safe=False)

def dyanamicResponse(request):
    name=request.GET.get("name","")
    city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name} from {city}")

def add(request):
    a=int(request.GET.get('a',4))
    b=int(request.GET.get('b',5))
    result=a+b
    return HttpResponse(f"The  sum  of {a} and {b} is {result}")


def sub(request):
    a=int(request.GET.get('a',4))
    b=int(request.GET.get('b',5))
    result=a-b
    return HttpResponse(f"The  sub  of {a} and {b} is {result}")


def mul(request):
    a=int(request.GET.get('a',4))
    b=int(request.GET.get('b',5))
    result=a*b
    return HttpResponse(f"The  mul is {a} and {b} is {result}")




    
    
    