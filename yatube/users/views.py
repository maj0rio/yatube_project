from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from post.models import Post


def login_view(request):
    template = 'users/login_view.html'
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=email, password=password)
            if user is not None:
                form.confirm_login_allowed(user)
                login(request, user)
                return redirect('users:myview')
            else:
                form.add_error("Неверный логин или пароль!")
    else:
        form = AuthenticationForm()

    content = {
        'form': form,
    }
    return render(request, template, content)


@login_required()
def myview(request):
    template = 'users/myview.html'
    posts = Post.objects.filter(author=request.user)
    content = {
        'posts': posts,
    }
    return render(request, template, content)


def create_user(request):
    error = ''
    template = 'users/create_user.html'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('post:index')
    else:
        form = CustomUserCreationForm()

    content = {
        'form': form,
        'error': error
    }
    return render(request, template, content)


