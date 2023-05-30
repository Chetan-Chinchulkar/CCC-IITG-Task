from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_list')  # Replace 'user_list' with the URL name of your user list view
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = ''
    
    return render(request, 'login.html', {'error_message': error_message})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})