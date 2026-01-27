from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)
        login(request, user)
    return render(request, 'myapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myapp/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request, user_id):
    profile = get_object_or_404(Profile, user__id=user_id)
    return render(request, 'myapp/profile.html', {'profile': profile})  

@login_required
def follow_user(request, user_id):
    target_profile = get_object_or_404(Profile, user__id=user_id)
    target_profile.followers.add(request.user)
    return redirect('profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    target_profile = get_object_or_404(Profile, user__id=user_id)
    target_profile.followers.remove(request.user)
    return redirect('profile', user_id=user_id)    
