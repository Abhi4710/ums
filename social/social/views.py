from django.shortcuts import render, reverse, HttpResponse, redirect, HttpResponseRedirect
from social.forms import UserLoginForm, UserRegistrationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django import forms



def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(request, username=username, password=password)
                if not user:
                    raise ValidationError("invalid_login")
                if user:
                    login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                form = UserLoginForm()
                return render(request, 'login.html', {'form': form})
    else:
        if request.method == 'GET':
            user = request.user
            if user.is_active:
                return redirect('home')
            else:
                form = UserLoginForm()
                return render(request, 'login.html', {'form': form})
    return HttpResponseRedirect(reverse('home'))


@login_required()
def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required()
def user_logout(request):
    if request.method == "POST":
        logout(request)
    else:
        logout(request)
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


def user_register(request):
    if request.method == 'POST':
        # if request is a post request the collect all the data from the form.
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password1 = request.POST["password1"]
            form.save()
            user = authenticate(request, username=username, password=password1)
            if user:
                login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
        args = {'form': form}
        if request.method == 'GET':
            user = request.user
            if user.is_active:
                return redirect('home')
            else:
                return render(request, 'register.html', args)


@login_required()
def user_edit(request):

    form = EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.profileuser)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'editprofile.html', {'form': form})
    else:
        return render(request, 'editprofile.html', {'form': form})
    return redirect('profile')


@login_required()
def user_del(request):
    user = request.user
    if user:
        user.delete()
    return redirect('home')


def pass_change(request):
    form = PasswordChangeForm(request.user)
    args = {'form': form}
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, request.user)
        if form.is_valid():
            user = User.objects.get(user=request.user)
            user.password = form.cleaned_data.get['new_password1']
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            return render(request, 'pass.html', args)
    else:
        return render(request, 'pass.html', args)



