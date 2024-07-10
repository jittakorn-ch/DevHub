from django.shortcuts import render, redirect
from main.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'main/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')

    context = {
        'register_form': form
    }
    return render(request, 'main/register.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('dashboard')

    context = {
        'login_form': form
    }
    return render(request, 'main/my_login.html', context)

def user_logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='user_login')
def dashboard(request):
    return render(request, 'main/dashboard.html')


