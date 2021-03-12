# from django import forms
#
# from apps.account.models import User
#
#
# class RegisterAccountModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'password', 'bio', 'website']
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.account.models import User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender', 'phone_number', 'bio', 'website')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender', 'phone_number', 'bio', 'website')

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']