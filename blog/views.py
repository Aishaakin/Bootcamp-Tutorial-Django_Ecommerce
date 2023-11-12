from django.shortcuts import render
from django.http import HttpResponse
from .models import PostContent

# Create your views here.

def BlogHome(request):
    data = { "title" : "Blog home page"}
    return render (request,"tests.html", data)
def ShopHome(request):
    data = { "title" : "Blog Shop page"}
    return render (request ,"shop.html", data)   

def BlogMain(request):
    data = { "title" : "Blog Main page"}
    return render (request ,"blogmain.html", data)    
def ViewData(request):    
    x = PostContent.objects.all()
    for i in x:
        print(i.title)
    return HttpResponse("<h2>Done !</h2>")    