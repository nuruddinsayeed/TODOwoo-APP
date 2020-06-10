from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'todo/home.html')


#Login Function
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form' : AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form' : AuthenticationForm(), 'error' : "User name or password is incorrect"})
        else:
            login(request, user)
            return redirect('currenttodos')


#Sign Up function
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form' : UserCreationForm(), 'error' : 'User name already been taken, please choose another username'})
        else:
            return render(request, 'todo/signupuser.html', {'form' : UserCreationForm(), 'error' : 'Password did not match'})



def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')
