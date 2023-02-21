from django.shortcuts import render

def index(request):
    template = 'post/index.html'
    text =  'Это главная страница'

    content = {
        'text': text,
    }

    return render(request, template, content)


def group_posts(request, pk):
    template = 'post/group_list.html'
    text = f'Здесь скоро появится информация о группах проекта Yatube.(проверка параметра {pk})'

    content = {
        'text': text,
    }
    return render(request, template, content)
