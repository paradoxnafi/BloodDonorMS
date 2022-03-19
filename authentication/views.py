from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def loginUser(request):

    return render(request, 'authentication/login.html')

def registerUser(request):
    if request.method == 'GET':
        return render(request, 'authentication/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homePage')
            except IntegrityError:
               return render(request, 'authentication/register.html', {'form': UserCreationForm(), 'error': 'The username is taken. Please try another username'})
        else:
            # password does not match
            return render(request, 'authentication/register.html', {'form': UserCreationForm(), 'error': 'Password does not match'})

def homePage(request):
    return render(request, 'post/home.html')