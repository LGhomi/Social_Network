from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ['created']