from django.contrib import admin

from apps.user.models import User,  Following


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['email', 'active']
    readonly_fields = ['created']


# @admin.register(FriendRequest)
# class FriendRequestAdmin(admin.ModelAdmin):
#     list_display = ['to_user', 'from_user']
#     readonly_fields = ['created']
@admin.register(Following)
class FollowingAdmin(admin.ModelAdmin):
    list_display = ['user']

