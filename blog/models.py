from django.db import models
from django.conf import settings
from django.urls import reverse
class Tag(models.Model):
    name = models.CharField('название',max_length=55,unique=True)
    slug = models.SlugField('slug',max_length=55,unique=True)

    class Meta:
        verbose_name = 'тег'
        ordering = ['name']
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
    
class Category(models.Model):
        name = models.CharField('название',max_length=80,unique=True)
        slug = models.SlugField('slug',max_length=90,unique=True)

        class Meta:
            verbose_name = 'категория'
            ordering = ['name']
            verbose_name_plural = 'категория'

        def __str__(self):
            return self.name


class Post(models.Model):
    title = models.CharField('заголовок',max_length=200)
    text = models.TextField('текст')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts',
    )

    tags = models.ManyToManyField(
            Tag,
            blank=True,
            related_name='posts',
            verbose_name='теги'
            )
    
    image1 = models.ImageField('изображение 1',upload_to='posts/',blank=True,null=True)
    image2 = models.ImageField('изображение 2',upload_to='posts/',blank=True,null=True)
    image3 = models.ImageField('изображение 3',upload_to='posts/',blank=True,null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='лайки',blank=True)

    created_at = models.DateTimeField('создано',auto_now_add=True)
    updated_at = models.DateTimeField('обновлено',auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    
    def __str__(self):
            return self.title
    
    def likes_count(self):
            return self.likes.count()
    
    def get_absolute_url(self):
            return reverse('blog:post_detail',kwargs={'pk':self.pk})