from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from config.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
User = get_user_model()

def home(request):
    return render(request, 'users/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)

def login_view(request):
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        raise PermissionDenied()
    
    context = {'user': user,
                'title': 'Информация о профиле'}
    return render(request, 'users/profile.html', context=context)
