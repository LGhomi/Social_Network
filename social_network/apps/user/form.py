from django import forms

from social_network.apps.user.models import User


class RegisterUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'password', 'bio', 'website']


class UserLoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
