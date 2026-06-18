from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','category','tags','image1','image2','image3')
        widgets = {
                    'text': forms.Textarea(attrs={'rows': 8}),
                    'tags':forms.CheckboxSelectMultiple(),
                    }