from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_user

app_name = 'users'

urlpatterns = [
    path('login/', create_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]