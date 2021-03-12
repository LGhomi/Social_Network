from django import template

#
# from apps.account.models import User
#


from apps.account.models import User, Friend_Request

register = template.Library()


@register.simple_tag(name='follower_cnt')
def count_follower(request):
    user = User.objects.get(id=request.user.id)
    return user.follower.count()


@register.simple_tag(name='following_cnt')
def count_followed(request):
    account = User.objects.get(id=request.user.id)
    return account.followed.count()


# @register.simple_tag(name='requests')
# def requests_list(request):
#     account = User.objects.get(id=request.user.id)
#     requests = Friend_Request.objects.get(to_user=account)
#     return requests

# @register.simple_tag(name='username')
# def username():
#     "return username of login account"
#     obj = User.objects.get(active=True)
#     return obj.email
