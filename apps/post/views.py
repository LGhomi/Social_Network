from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.generics import get_object_or_404

from .forms import PostForm
from .models import Post
from ..user.models import User


class PostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post/add_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            post_obj = Post(**validated_data)
            post_obj.save()
            return redirect('ok')
        return render(request, 'post/add_post.html', {'form': form})


# def add_post(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     form = PostForm(request.POST, instance=user)
#     if form.is_valid():
#         form.save()


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'


class PagedPostList(ListView):
    paginate_by = 2
    model = Post
    template_name = 'post/paged_post_list.html'


class PostDetail(DetailView):
    model = Post