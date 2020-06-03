from django.shortcuts import render,redirect
from .models import CounterModel

# Create your views here.
#num = 0
def helloworld(request):
    #global num
    obj = CounterModel.objects.filter(id = 1)[0]
    print(type(obj))
    print(obj)
    num = obj.number
    context = {'num': num}
    return render(request, "helloworld.html",context)
    

def hellostudent(request):
    return render(request, "hellostudent.html")


def decrement(request):
    #global num 
    #num = num - 1
    #context = {'num': num}
    #return render(request, "helloworld.html", context)
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) - 1  
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    #global num
    #num = 0
    #context = {'num': num}
    #return render(request,"helloworld.html", context)
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def increment(request):
    #global num
    #num = num + 1
    #context = {'num' : num }
    #return render(request, "helloworld.html", context)
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])