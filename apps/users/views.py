from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        ...
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password1')
        passwort_2 = request.POST.get('password2')
        if password_1 != passwort_2:
            return render(request, 'register.html', {'error': 'Passwort do not match'})
        else:
            user = User.objects.create_user(username = username, email = email, password = password_1)
            user.save()
            login(request, user)
            return redirect('home')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')
