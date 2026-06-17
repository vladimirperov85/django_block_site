from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
Добавьте сюда дополнительные поля : телефон,город,аварка,
"""
    phone = models.CharField('телефон',max_length=20, blank=True, help_text='Можно оставить пустым')
    city = models.CharField('город',max_length=100, blank=True)
    avatar = models.ImageField('аватар',upload_to='avatars/',blank=True, null=True)

def __str__(self):
    return self.username