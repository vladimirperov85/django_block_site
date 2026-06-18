from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Post
from blog.forms import PostForm 

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Пост создан!')
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', context = {'form':form,'title': 'Новый пост'})
    

def post_detail(request,pk):
    post = get_object_or_404(
            Post.objects.select_related('author','category').prefetch_related('tags', 'likes'),
            pk=pk,
    )
    return render(request, 'blog/post_detail.html', context = {'post':post})