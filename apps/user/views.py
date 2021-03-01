import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from apps.user.form import RegisterUserModelForm, UserLoginModelForm
from apps.user.models import User, Following


class UserList(ListView):
    """
        show list of users
    """
    model = User


class UserDetail(DetailView):
    """
        show detail of users
    """
    model = User


class Search(View):
    """
    The user can search among other users
    """

    def get(self, request):
        search_text = request.GET.get('search_text')
        users = None
        results = User.objects.exclude(active=True)  # name of the active user is not displayed in the list
        user = User.objects.get(active=True)
        username = user.email  # To display the user name in her/his profile
        if search_text:
            users = User.objects.filter(email__icontains=search_text, active=False)
        return render(request, 'user/search.html', {'users': users, "results": results, 'username': username})


class UserView(View):
    """
    To register a user
    """

    def get(self, request):
        """
        Show registration form
        """
        form = RegisterUserModelForm()
        return render(request, 'user/register_user.html', {'form': form})

    def post(self, request):
        """
            Create a new user
        """
        form = RegisterUserModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            user_obj = User(**validated_data)
            user_obj.save()
            return redirect('login')
        return render(request, 'user/register_user.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', {'message': '', 'user': ''})

    def post(self, request):
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(active=True):
            # message = ' is login!!'
            # user = User.objects.get(active=True)
            # username = user.email
            return redirect('profile')
        else:
            if username and password:
                if User.objects.filter(email=username):
                    user = User.objects.get(email=username)
                    username = user.email
                    if user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                        User.objects.filter(email=username).update(active=True)
                        return redirect('profile')
                    else:
                        username = ''
                        message = 'wrong password!!!'
                else:
                    username = ''
                    message = 'Invalid email or password!!!'
            else:
                username = ''
                message = 'Email or password is empty!!!'
        return render(request, 'user/login.html', {'message': message, 'user': username})


class LogoutView(View):
    """
    When one user logs in, another user cannot log in, For this reason, this display is designed for user exit
    """

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
    """
    To display each user's name in their profile
    """

    def get(self, request):
        user = User.objects.get(active=True)
        username = user.email
        return render(request, 'user/profile.html', {'username': username})


# class follow(View):
#
#     def get(self, request):
#         from_user = User.objects.get(active=True)
#         username = user.email
#         return render(request, 'user/profile.html', {'username': username})


def follow(request, pk):
    main_user = User.objects.get(active=True)
    to_follow = User.objects.get(pk=pk)
    following = Following.objects.filter(user=main_user, followed=to_follow)
    followerr = Following.objects.filter(user=to_follow, follower=main_user)
    is_following = True if following else False
    is_followerr = True if followerr else False

    if not is_following:
        Following.follow(main_user, to_follow)

    if not is_followerr:
        Following.follow_back(to_follow,main_user)

    return redirect('user_detail', pk=pk)
