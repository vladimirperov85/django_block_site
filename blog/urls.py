from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('posts/', views.post_list, name='post_list'),  

    # Статичные действия с постами — ВСЕГДА до <int:pk>
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/me/', views.my_posts, name='my_posts'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Посты пользователя
    path('users/<int:user_id>/posts/', views.user_posts, name='users_posts'),  
]