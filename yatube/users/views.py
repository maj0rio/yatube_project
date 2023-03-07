from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser


def create_user(request):
    error = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            error = 'Форма была неверной'
            form = CustomUserCreationForm(request.POST)

    else:
        form = CustomUserCreationForm()

    content = {
        'form': form,
        'error': error
    }

    return render(request, 'users/login.html', content)


