from django import template

from ..models import Post
from ...user.models import User

register = template.Library()


@register.simple_tag(name='p_cnt')
def count_post():
    "count posts of user"
    obj = User.objects.get(active=True)
    return Post.objects.filter(user_id=obj.pk).count()


@register.simple_tag(name='username')
def username():
    "return username of login user"
    obj = User.objects.get(active=True)
    return obj.email


@register.simple_tag(name='l_cnt')
def count_like(pk):
    "count likes of post"
    post = Post.objects.get(pk=pk)
    return post.like_set.count()


@register.inclusion_tag('post/post_comments.html')
def show_comments(pk):
    "show comment of post"
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    return {'comments': comments}


@register.inclusion_tag('post/user_post.html')
def user_post(pk):
    "show post of user"
    user = User.objects.get(pk=pk)
    posts = user.post_set.all()
    return {'posts': posts}
