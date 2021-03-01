from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.generics import get_object_or_404

from .forms import PostForm
from .models import Post, Like, Comment
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


class UserName(View):
    """
    To display each user's name in their profile
    """

    def get(self, request):
        user = User.objects.get(active=True)
        username = user.email
        return render(request, 'user/profile.html', {'username': username})


def like(request, pk):
    main_user = User.objects.get(active=True)
    to_like = Post.objects.get(pk=pk)
    if Like.objects.filter(post_id_id=to_like.id, user_id_id=main_user.id):
        return redirect('post_detail', pk=pk)
    else:
        like = Like(post_id_id=to_like.id, user_id_id=main_user.id)
        like.save()
        return redirect('post_detail', pk=pk)


class AddComment(View ):

    def post(self, request, pk):
        user_obj = User.objects.get(active=True)
        to_comment = Post.objects.get(pk=pk)
        note = request.POST.get("note")
        # is_comment = request.POST.get("comment_btn")
        print(note)
        if note:
            comment = Comment.objects.create(note=note, post_id_id=to_comment.id, user_id_id=user_obj.id)
            comment.save()
        return redirect('post_detail',pk=pk)


class FollowingPost(View):
    def get(self, request):
        posts = []
        person = User.objects.get(active=True)
        following = person.followed.all()
        if following:
            for f in following:
                f1 = User.objects.get(email=f)
                for post in f1.post_set.all():
                    posts.append(post)
            context = {'posts': posts, 'username': person.email}
            return render(request, 'post/following_post.html', context)
        else:
            return render(request, 'post/following_post.html')



# c=Comment(note='hiii',post_id_id=4,user_id_id=6)
# c.save()
