from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
    template = 'post/index.html'
    text = ('Yatube - это платформа, созданная для того, ' 
            'чтобы люди могли делиться своими интересными '
            'историями с остальными!')

    return render(request, template)


def group_posts(request, pk):
    template = 'post/group_list.html'
    text = (f'Здесь скоро появится информация о группах проекта Yatube.'
            f'(проверка параметра {pk})')

    content = {
        'text': text,
    }
    return render(request, template, content)


def last_posts(request):
    template = 'post/last_posts.html'
    posts_list = Post.objects.all()

    content = {
        'posts': posts_list
    }
    return render(request, template, content)


@login_required()
def create_post(request):
    template = 'post/create_post.html'

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('users:myview')
    else:
        form = PostForm()

    content = {
        'form': form,
    }
    return render(request, template, content)

