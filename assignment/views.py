from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from assignment.forms import SignUpForm
from assignment.models import Profile
from signup.settings import LOGIN_REDIRECT_URL


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


def userprofiledetails(request):
    """user profile view"""
    user_profile = Profile.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})
