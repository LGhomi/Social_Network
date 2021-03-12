from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, RedirectView, UpdateView

from apps.account.form import AccountCreationForm, UserUpdateForm
from django.contrib import messages, auth

from apps.account.models import User, Following, Friend_Request


class RegisterView(CreateView):
    form_class = AccountCreationForm
    success_url = 'login'
    template_name = 'account/register_user.html'

    def post(self, request, **kwargs):
        messages.success(request, 'User was successfully created.')
        return super(RegisterView, self).post(request)


class UserList(ListView):
    """
        show list of users
    """
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserDetail(DetailView):
    """
        show detail of users
    """
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class Search(View):
    """
    The account can search among other users
    """

    def get(self, request):
        search_text = request.GET.get('search_text')
        users = None
        results = User.objects.exclude(id=request.user.id)  # name of the active account is not displayed in the list
        # users = User.objects.get(id=request.user.id)
        # username = account.email  # To display the account name in her/his profile
        if search_text:
            users = User.objects.filter(email__icontains=search_text)
        return render(request, 'account/search.html', {'users': users, "results": results})


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class UserName(View):
    """
    To display each account's name in their profile
    """

    def get(self, request):
        username = User.email
        return render(request, 'account/profile.html', {'username': username})


class FollowersList(LoginRequiredMixin, View):
    """
    Each account can see their list of followers
    """

    def get(self, request):
        person = User.objects.get(id=request.user.id)
        users = person.follower.all()
        context = {'users': users, 'username': person.email}
        return render(request, 'account/follower_list.html', context)


class FollowingList(View):
    """
    Each account can see their list of following
    """

    def get(self, request):
        person = User.objects.get(id=request.user.id)
        users = person.followed.all()
        context = {'users': users, 'username': person.email}
        return render(request, 'account/followed_list.html', context)


class UpdateUser(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = '/'
    template_name = 'account/edit_user.html'


@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('request sent')
    else:
        return HttpResponse('request was already sent')


@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        to_user = friend_request.to_user
        from_user = friend_request.from_user
        # main_user = User.objects.get(id=request.user.id)
        # to_follow = User.objects.get(pk=pk)
        following = Following.objects.filter(user=from_user, followed=to_user)
        followerr = Following.objects.filter(user=to_user, follower=from_user)
        is_following = True if following else False
        is_followerr = True if followerr else False

        if not is_following:
            Following.follow(from_user, to_user)

        if not is_followerr:
            Following.follow_back(to_user, from_user)

        return HttpResponse('request accepted')
    else:
        return HttpResponse('request not accepted')


class RequestList(View):

    def get(self, request):
        person = User.objects.get(id=request.user.id)
        users = person.to_user.all()
        context = {'users': users, 'username': person.email}
        return render(request, 'account/requests.html', context)
