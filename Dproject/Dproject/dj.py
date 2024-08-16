from django.http import HttpResponse
from django.shortcuts import render

def registerpage(request):
    return render(request,"registerpage.html")
def loginpage(request):
    return render(request,"loginpage.html")
def ram(request):
    return render(request,"ram.html")


