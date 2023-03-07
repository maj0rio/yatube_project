from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    template = 'post/index.html'
    text =  'Yatube - это платформа, созданная для того, чтобы люди могли делиться своими интересными историями с остальными!'


    return render(request, template)


def group_posts(request, pk):
    template = 'post/group_list.html'
    text = f'Здесь скоро появится информация о группах проекта Yatube.(проверка параметра {pk})'

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

def create_post(request):
    form = PostForm()

    content = {
        'form': form,
    }
    return render()

