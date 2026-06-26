from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from blog.models import Post, Category,Tag
from blog.forms import PostForm 
from django.db.models import Q,Count
from django.contrib.auth.decorators import login_required

@login_required
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
        
    
    return render(request, 'blog/post_form.html', context = {'form':form,'title': 'Новый пост'})
    

def post_detail(request,pk):
    post = get_object_or_404(
            Post.objects.select_related('author','category').prefetch_related('tags', 'likes'),
            pk=pk,
    )
    return render(request, 'blog/post_detail.html', context = {'post':post})


def post_list(request):
    """ Главная страница со списком постов"""
    """Фильтрация, сортировка"""
    # получаем список постов
    # select_related - подгружает связанные модели
    # prefetch_related - подгружает связанные модели ManyToMany
    posts = Post.objects.select_related('author','category').prefetch_related('tags', 'likes')
    # передаем в шаблон
    # получаем из форм ввода в GET запросе
    query = request.GET.get('q',"").strip()
    author_id = request.GET.get('author',"")
    category_id = request.GET.get('category',"")
    tag_id = request.GET.get('tag',"")
    sort = request.GET.get('sort',"-created_at")

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(text__icontains=query))
    if author_id:
        posts = posts.filter(author_id=author_id)
    if category_id:
        posts = posts.filter(category_id=category_id)
    if tag_id:
        posts = posts.filter(tags__id=tag_id)
    # annotations - добавляет поле в запрос
    posts = posts.annotate(likes_count=Count('likes'))

    allowed_sort_fields = {
        '-created_at': '-created_at',
        'created_at': 'created_at',
        'title': 'title',
        '-title': '-title',
        '-likes_count': '-likes_count',
        'likes_count': 'likes_count'
        }
    posts = posts.order_by(allowed_sort_fields.get(sort, '-created_at'))
    context = {
        'posts': posts,
        'query': query,
        'categories': Category.objects.all(),
        'authors': get_user_model().objects.all().order_by('username'),
        'tags': Tag.objects.all(),
        'selected_author': author_id,
        'selected_category': category_id,
        'selected_tag': tag_id,
        'selected_sort': sort,
        'page_heading': 'Посты',
        'page_description':'Читаете посты, ищите по тексту, фильтруйте по автору и тегам',

    }
    return render(request, 'blog/post_list.html', context=context)

def user_posts(request, user_id):
    author = get_object_or_404(get_user_model(), pk=user_id)
    posts = (
            Post.objects.select_related('author', 'category')
                .prefetch_related('tags', 'likes')
                .filter(author=author)
                .annotate(likes_count=Count('likes'))
                .order_by('-created_at')
    )
    context = {'posts': posts,
            'hide_filters': True,
            'page_heading': f'Посты {author.username}',
            'page_description':'Читаете посты, ищите по тексту, фильтруйте по автору и тегам',
            }
    return render(request, 'blog/post_list.html', context=context)

@login_required
def my_posts(request):
    
    posts = (
            Post.objects.select_related('author', 'category')
                .prefetch_related('tags', 'likes')
                .filter(author=request.user)
                .annotate(likes_count=Count('likes'))
                .order_by('-created_at')
    )
    context = {'posts': posts,
            'hide_filters': True,
            'page_heading': 'Мои посты',
            'page_description':'Все опубликованные мной посты',
            }
    return render(request, 'blog/post_list.html', context=context)

@login_required
def post_update(request, pk):
    # редактирование поста(толькл свои)
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'Вы не можете редактировать чужие посты!')
        return redirect('blog:post_detail', pk=post.pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Пост успешно обновлен!')
        return redirect('blog:post_detail', pk=post.pk)

    return render(request, 'blog/post_form.html', context={'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and not request.user.is_staff:
        messages.error(request, 'Вы не можете удалять чужие посты!')
        return redirect(post)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост успешно удален!')
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', context={'post':post})