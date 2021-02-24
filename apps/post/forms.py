from django import forms

from apps.post.models import Post
from apps.user.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'user_id']
