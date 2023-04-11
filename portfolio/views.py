from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def portfolio(request):
    return render(request,"portfolio.html")
def aboutUs(request):
    return render(request,"about.html")
