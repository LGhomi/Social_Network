# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
# from django.contrib.auth.models import User
#
# from apps.account.models import Account
#
#
# class AccountInline(admin.StackedInline):
#     model = Account
#     can_delete = False
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (AccountInline,)
#     # Re-register UserAdmin
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Following


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Following)
class FollowingAdmin(admin.ModelAdmin):
    list_display = ['user']