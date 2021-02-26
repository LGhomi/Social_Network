from django import template

from ..models import Post

register = template.Library()


@register.simple_tag(name='p_cnt')
def count_post(user_pk):
    return Post.objects.count(user_id=user_pk)