from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.generics import get_object_or_404

from .forms import PostForm
from .models import Post
from ..user.models import User


class PostView(View):
    """
    add new post
    """

    def get(self, request):
        user = User.objects.get(active=True)
        form = PostForm()
        return render(request, 'post/add_post.html', {'form': form, 'username': user.email})

    def post(self, request):
        """
        :param request: request for create new post
        :return: save post and send username to template
        """
        user = User.objects.get(active=True)
        form = PostForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            post_obj = Post(**validated_data)
            post_obj.save()
            return redirect('ok')
        return render(request, 'post/add_post.html', {'form': form, 'username': user.email})


class PostList(ListView):
    """
    class view of post return all posts
    """
    model = Post
    context_object_name = 'post_list'


class MyPostList(View):
    def get(self, request):
        """
        :param request: request to show user's posts
        :return: title list of user's posts
        """
        user = User.objects.get(active=True)
        my_post_list = Post.objects.filter(user_id=user.pk)
        context = {'my_post_list': my_post_list, 'username': user.email}
        return render(request, 'post/my_post_list.html', context)


class PagedPostList(ListView):
    """
    pagination all posts
    """
    paginate_by = 2
    template_name = 'post/paged_post_list.html'


class PostDetail(DetailView):
    """
    show detail of post.
    """
    model = Post
