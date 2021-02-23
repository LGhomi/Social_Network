from django.shortcuts import render, redirect
from django.views import View

from social_network.apps.user.form import UserLoginModelForm, RegisterUserModelForm
from social_network.apps.user.models import User


class Search(View):
    def get(self, request):
        search_text = request.GET.get('search_text')
        users = None
        if search_text:
            users = User.objects.filter(email__icontains=search_text)
        return render(request, 'user/search.html', {'users': users})


class UserView(View):
    def get(self, request):
        form = RegisterUserModelForm()
        return render(request, 'user/register_user.html', {'form': form})

    def post(self, request):
        form = RegisterUserModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            user_obj = User(**validated_data)
            user_obj.save()
            return redirect('ok')
        return render(request, 'user/register_user.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginModelForm()
        return render(request, 'user/user_login.html', {'form': form})

    def post(self, request):
        form = UserLoginModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            user_obj = User(**validated_data)
            user_obj.save()
            return redirect('ok')
        return render(request, 'user/user_login.html', {'form': form})
