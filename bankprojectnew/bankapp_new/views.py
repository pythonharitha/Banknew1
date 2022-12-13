from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from bankapp_new.forms import NewCreationForm


def index(request):
    return render(request,"index.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")

def home(request):
    return render(request,"home.html")

def create_view(request):
    form=NewCreationForm()
    if request.method=='POST':
        form=NewCreationForm(request.POST)
        if form.is_valid():
            return redirect('new')
    return render(request,'list.html',{'form':form})

def new(request):
    return render(request,'new.html')


def logout(request):
    return HttpResponse('/login')