from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('posts/<int:pk>/',views.post_detail,name = 'post_detail'),
    path('posts/create',views.post_create,name = 'post_create'),
    path('posts/',views.post_list, name='post_list'),
    path('',views.post_list,name='main'),

]