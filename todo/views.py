from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# Create your views here.
##home
def home(request):
    return render(request, 'todo/home.html')

#aytg
def signupUser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        pass1= request.POST['password1']
        pass2= request.POST['password2']
        if(pass1 == pass2):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=pass1)
                user.save()
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Username alrady taken"})

        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Passwords didn't match"})
            #tell pass not match

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginUser(request):
    if request.method =='GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        name = request.POST['username']
        passo = request.POST['password']
        user = authenticate(request, username=name, password=passo)
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('current')        
            

def currentTodo(request):
    return render(request, 'todo/currenttodos.html', {'form': UserCreationForm()})

