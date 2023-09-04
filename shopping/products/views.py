from django.shortcuts import render
from django.http import HttpResponse
from.models import items

# Create your views here.
def index(request):
    products=items.objects.all()
    return render(request,'index.html',{'products':products})


def about(request):
    return HttpResponse('<h1>THIS IS ABOUT</h1>')
