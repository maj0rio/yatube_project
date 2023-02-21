from django.urls import path, re_path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:pk>', views.group_posts, name='groups')

]