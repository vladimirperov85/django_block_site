from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/<int:pk>/', views.user_profile, name='profile'),
    
    ]
