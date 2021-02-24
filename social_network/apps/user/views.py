import hashlib

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from social_network.apps.user.form import RegisterUserModelForm
from social_network.apps.user.models import User


class UserList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


class Search(View):
    def get(self, request):
        search_text = request.GET.get('search_text')
        users = None
        if search_text:
            users = User.objects.filter(email__icontains=search_text)
        return render(request, 'profile.html', {'users': users})


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
            return redirect('profile')
        return render(request, 'user/register_user.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        return render(request, 'user/index.html')

    def post(self, request):
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user_obj = User.objects.get(email=username)
            if user_obj.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                return redirect('profile')
                # return render(request, '../templates/profile.html', {'username': username})
            else:
                message = 'Invalid email or password!!!'
        else:
            message = 'Email or password is empty!!!'
        return render(request, 'user/index.html', {'message': message})
