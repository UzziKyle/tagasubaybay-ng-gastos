from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def sign_in(request):
    context = {}
    context['form'] = LoginForm()
    
    if request.method == 'GET':        
        if request.user.is_authenticated:
            return redirect('home')
        
        return render(request, 'users/login.html', context)
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('home') 
                  
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', context)
    
    
def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')


def sign_up(request):
    context = {}
    
    if request.method == 'GET':
        form = RegisterForm()
        context['form'] = form
        return render(request, 'users/register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('home')
        
        else:
            form = RegisterForm()
            context['form'] = form
            return render(request, 'users/register.html', context)
