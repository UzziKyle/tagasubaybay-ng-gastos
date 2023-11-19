from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

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