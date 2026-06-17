from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """ Форма регистрации пользователя - наследуемся от стандартной формы регистрации 
    что бы не писать проверки пароля вручную"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'city', 'avatar','password1','password2')

class CustomUserChangeForm(forms.ModelForm):
    '''Форма редактирования профиля пользователя(кроме пароля)'''

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'city', 'avatar')
