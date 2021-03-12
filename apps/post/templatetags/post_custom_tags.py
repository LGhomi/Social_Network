from django import template

from ..models import Post

register = template.Library()


@register.simple_tag(name='p_cnt')
def count_post(id):
    "count posts of user"
    return Post.objects.filter(account_id=id).count()


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
def user_post(user):
    "show post of user"
    posts = user.post_set.all()
    return {'posts': posts}
