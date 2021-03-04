from django import template

from apps.user.models import User

register = template.Library()


@register.simple_tag(name='follower_cnt')
def count_follower():
    user = User.objects.get(active=True)
    return user.follower.count()


@register.simple_tag(name='following_cnt')
def count_followed():
    user = User.objects.get(active=True)
    return user.followed.count()
