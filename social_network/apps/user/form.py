from django import forms

from apps.user.models import User


class RegisterUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'password', 'bio', 'website']

