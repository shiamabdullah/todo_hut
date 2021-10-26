from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
# Create your views here.
def signupUser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        pass1= request.POST['password1']
        pass2= request.POST['password2']
        if(pass1 == pass2):
            try:
                user = User.objects.create_user(request.POST['username'], pass1)
                user.save()
                login(request,user)
                return redirect(currentTodo)
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Username alrady taken"})

        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Passwords didn't match"})
            #tell pass not match

def currentTodo(request):
    return render(request, 'todo/currenttodos.html', {'form': UserCreationForm()})
