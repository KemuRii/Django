from django.shortcuts import render
from django.contrib.auth.models import User



def homepage(request):
    return render(request, 'homepage.html')

def addRegister(request):
    username=request.POST['username']
    email=request.POST['email']
    password_1=request.POST['password']
    password_2=request.POST['Confirm password']

    user=User.objects.create_user(
        username=username,
        email=email,
        password=password_1,
        )
    user.save()
    return render(request, 'homepage.html')

def login_page(request):
    return render(request, 'login_page.html')

def create_room(request):
    return render(request, 'create_room.html')

def enter_room(request):
    return render(request, 'enter_room.html')

