from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from .forms import RegisterForm

# Create your views here.
def handle_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/todolist')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) 
                  
        
def handle_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form': form})
            
def handle_logout(request):
    logout(request)
    return redirect('/login')