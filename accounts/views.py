from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            #Login was successful
            auth.login(request, user)
            #Send a message of successful login
            return redirect('dashboard')
        else:
            return redirect('login')
        #else show some kind of an error
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        #show some kind of a message here
        return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                #show an error saying that the email has already been used
                print('email problem')
                return redirect('register')
            else:
                if User.objects.filter(username=username).exists():
                    #show an error saying that the username has already been used
                    print('username problem')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    print('cool')
                    #show some kind of a message saying taht the user has been registered
                    return redirect('login')
        else:
            print('password problem')
            #print that the passwords don't match
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
