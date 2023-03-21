from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_user, myview, login_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('myview/', myview, name='myview'),
    path('create_user/', create_user, name='create_user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]