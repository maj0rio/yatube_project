from django.urls import path
from .views import index, group_posts, last_posts, create_post

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('group/<slug:pk>/', group_posts, name='groups'),
    path('last_posts/', last_posts, name='last_posts'),
    path('create_post/', create_post, name='create_post'),

]