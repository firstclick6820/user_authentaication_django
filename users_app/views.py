from tkinter.tix import IMMEDIATE
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.


def home_page(request):
    context = {}
    return render(request, 'users_app/index.html', context)



def user_login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS,"You have already Logged in!")
        return redirect('home_page')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You have logged in successfully!')
            return redirect('home_page')
        else:
            messages.add_message(request, messages.WARNING, 'Wrong Cordentials, please try again!')
            return redirect('user_login')
    else:
        return render(request, 'users_app/index.html')



def user_regiser(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS,"You have already Logged in!")
        return redirect('user_login')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Your account created Successfully.')
            return redirect('home_page')
        else:
            messages.add_message(request, messages.WARNING, 'Something went wrong, try again!')
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'authenticate/user_register.html', context)



def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You have logged out successfully.")
    return redirect('home_page')