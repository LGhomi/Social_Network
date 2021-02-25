import hashlib

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from apps.user.form import RegisterUserModelForm, UserLoginModelForm
from apps.user.models import User


class UserList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


class Search(View):
    def get(self, request):
        search_text = request.GET.get('search_text')
        users = None
        user = User.objects.get(active=True)
        username = user.email
        if search_text:
            users = User.objects.filter(email__icontains=search_text)
        return render(request, 'user/search.html', {'users': users, 'username': username})


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
        return render(request, 'user/login.html')

    def post(self, request):
        message = ''
        user = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if User.objects.filter(email=username):
                user = User.objects.get(email=username)
                # message = str(user_obj)
                if User.objects.filter(active=True):
                    message = ' is login!!'
                    user = User.objects.get(active=True)
                    # return redirect('profile')
                else:
                    message = 'false pass!!!'
                    if user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                        User.objects.filter(email=username).update(active=True)
                        return redirect('profile')
            else:
                message = 'Invalid email or password!!!'
        else:
            message = 'Email or password is empty!!!'
        return render(request, 'user/login.html', {'message': message, 'user': user.email})


class LogoutView(View):
    def get(self, request):
        user = User.objects.get(active=True)
        return render(request, 'user/logout.html', {'username': user.email})

    def post(self, request):
        user_obj = User.objects.get(active=True)
        print(user_obj)
        is_logout = request.POST.get("logout")
        if is_logout:
            user_obj.active = False
            User.objects.filter(active=True).update(active=False)
        return redirect('login')


class UserName(View):
    def get(self, request):
        user = User.objects.get(active=True)
        username = user.email
        return render(request, 'user/profile.html', {'username': username})
