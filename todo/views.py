from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from todo.models import Todo
from .forms import TodoForm
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
    todos = Todo.objects.filter(todoCreator= request.user, completedAt__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})

def createTodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newTodo = form.save(commit=False) #creating newTOdo and commit false ensures it doesn't go to db
            newTodo.todoCreator = request.user #registering to the user
            newTodo.save()
            return redirect('current')        
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error':'Value Error. Try again'})



def viewTodo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodos.html', {'todo': todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo) #send the instance as well as it contains the user_field it points to the obj
            form.save()
            return redirect(currentTodo)

        except ValueError:
            return render(request, 'todo/viewtodos.html', {'todo': todo, 'form':form, 'error': 'value error'})
