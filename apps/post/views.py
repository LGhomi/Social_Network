from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import PostForm
from .models import Post, Like, Comment
from ..account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class MyPostList(View):
    def get(self, request):
        """
        :param request: request to show user's posts
        :return: title list of user's posts
        """
        user = request.user
        my_post_list = Post.objects.filter(account_id=user)
        context = {'my_post_list': my_post_list}
        return render(request, 'post/my_post_list.html', context)


class PostDetail(DetailView):
    """
    show detail of post.
    """
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class AddPostView(LoginRequiredMixin, CreateView):
    """
    add new post
    """
    form_class = PostForm
    template_name = 'post/add_new_post.html'
    success_url = '/profile/'

    def post(self, request, **kwargs):
        """
        :param request: request for create new post
        :return: save post and send username to template
        """

        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = Post(**form.cleaned_data, account_id=request.user)
            post.save()
            messages.success(request, "Post saved!")
            return redirect('/profile/')
        return render(request, 'post/add_new_post.html')


def success(request):
    return HttpResponse('successfully uploaded')
    #
    # class LikeView(View):
    #     """
    #
    #     Like other users' posts
    #     """
    #
    #     def get(self, request, pk):
    #         post = Post.objects.get(pk=pk)
    #         if post.like_set.filter(user_id_id=request.user.id):
    #             button = "dislike"
    #         else:
    #             button = "like"
    #         return render('post_detail', {'button': button})
    #
    #     def post(self, request, pk):
    #         post = Post.objects.get(pk=pk)
    #         like = Like(post_id_id=post.id, user_id_id=request.user.id)
    #         if Like.objects.get(post_id_id=post.id, user_id_id=request.user.id):
    #             like = Like.objects.de(post_id_id=post.id, user_id_id=request.user.id)
    #             like.delete()
    #         else:
    #             like.save()
    #         return redirect('post_detail', pk=pk)


def like(request, pk):
    """

    Like other users' posts
    """
    main_user = request.user
    to_like = Post.objects.get(pk=pk)
    if Like.objects.filter(post_id_id=to_like.id, user_id_id=main_user.id):
        return redirect('post_detail', pk=pk)
    else:
        like = Like(post_id_id=to_like.id, user_id_id=main_user.id)
        like.save()
        return redirect('post_detail', pk=pk)


class AddComment(View):
    """

Leave a comment for other users' posts
    """

    def post(self, request, pk):
        user_obj = request.user
        to_comment = Post.objects.get(pk=pk)
        note = request.POST.get("note")
        # is_comment = request.POST.get("comment_btn")
        print(note)
        if note:
            comment = Comment.objects.create(note=note, post_id_id=to_comment.id, user_id_id=user_obj.id)
            comment.save()
        return redirect('post_detail', pk=pk)


class FollowingPost(View):
    """
    Each user can see other users' posts in their profile
    """

    def get(self, request):
        posts = []
        person = request.user
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


class UpdatePost(UpdateView):
    model = Post
    template_name = 'post/edit_post.html'
    fields = ['title', 'content', 'image']
    success_url = '/post/'


# def post_delete(pk):
#     instance = Post.objects.get(id=pk)
#     instance.delete()  # or save edits
#     # messages.success(request, "Successfully Deleted")
#     return redirect("/post/")

# @login_required
# def post_delete(request, pk=None):
#     instance = get_object_or_404(Post, pk=pk)
#     if request.user == Post.account_id:
#         instance.delete()  # or save edits
#         messages.success(request, "Successfully Deleted")
#         return redirect("/post/")
# else:
#     raise PermissionDenied  # import it from django.core.exceptions

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_detail',  pk=pk)


def comment_delete(request, pk):
    instance = get_object_or_404(Comment, pk=pk)
    pk = instance.post_id.pk
    instance.delete()  # or save edits
    # messages.success(request, "Successfully Deleted")
    return redirect('post_detail',  pk=pk)
