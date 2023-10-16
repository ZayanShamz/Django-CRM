from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):

    # Check logging in
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']

        print(username, passwd)

        # Authenticate
        user = authenticate(request, username=username , password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful...")
            return redirect('home')
        else:
            messages.error(request, "Chek your password or Username")
            return redirect('home') 
    else:
        return render(request, 'home.html', {})

def logout_usr(request):
    logout(request)
    messages.success(request, "Logout successful...")
    return redirect('home') 

def register_usr(request):
    return render(request, 'register.html', {})