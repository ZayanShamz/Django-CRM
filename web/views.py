from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import is_valid_path

from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):

    records = Record.objects.all()

    # Check logging in
    if request.method == 'POST':
        username = request.POST['username']
        # passwd = request.POST['password']
        passwd = request.POST.get('pass', False)
        print(passwd)

        # Authenticate
        user = authenticate(request, username=username , password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful...")
            return redirect('home')
        else:
            messages.error(request, "Check your password or Username")
            return redirect('home') 
    else:
        return render(request, 'home.html', {'records': records})
    

def cust_record(request, pk):
    if request.user.is_authenticated:
        cust_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'cust_record': cust_record})
    else:
        messages.error(request, "You Must Be Logged In!")
        return redirect('home') 
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In!")
        return redirect('home') 
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In!")
        return redirect('home') 


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.error(request, "Record Deleted!")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In!")
        return redirect('home') 

def logout_usr(request):
    logout(request)
    messages.success(request, "Logout successful...")
    return redirect('home') 

def register_usr(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            # authenticate and login
            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password1']

            user = authenticate(username=username, password=passwd)
            login(request, user)
            messages.error(request, "Registration successful")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})