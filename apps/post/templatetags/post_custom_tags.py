from django import template

from ..models import Post
from ...account.models import Friend_Request

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
def show_comments(pk, user):
    "show comment of post"
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    return {'comments': comments, 'user': user}


@register.inclusion_tag('post/user_post.html')
def user_post(user):
    "show post of user"
    posts = user.post_set.all()
    return {'posts': posts}

# @register.inclusion_tag('account/user_detail.html')
# def check_request(pk):
#     "show comment of post"
#     req = Friend_Request.objects.get(from_user_id=pk)
#     # comments = post.comment_set.all()
#     return {'comments': comments}
