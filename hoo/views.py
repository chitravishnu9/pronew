
from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def signup(request):
    return render(request,"signup.html")

def register(request):
    return render(request,"register.html")

def newpassword(request):
    return render(request,"newpassword.html")

def logout(request):
    return render(request,"logout.html")

