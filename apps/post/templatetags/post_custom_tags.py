from django import template

from ..models import Post
from ...user.models import User

register = template.Library()


# @register.simple_tag(name='p_cnt')
# def count_post():
#     obj = User.objects.get(active=True)
#     obj_id = obj.pk
#     return Post.objects.count(user_id=obj_id)
