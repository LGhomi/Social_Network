from django.urls import path

from apps.post import views
from apps.post.views import PostView, PostList, PostDetail, PagedPostList, MyPostList, AddComment,FollowingPost

urlpatterns = [
    path('', PostList.as_view(), name="posts"),
    path('My_post_list/', MyPostList.as_view(), name="my_post_list"),
    path('<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('<int:pk>/like', views.like, name="like"),
    path('<int:pk>/comment', AddComment.as_view(), name="comment"),
    # path('<int:pk>/comment', views.comment, name="comment"),
    path('add_post/', PostView.as_view(), name="add_new_post"),
    path('paged_post_list/', PagedPostList.as_view(), name='paged_post_list'),
    path('following_post/', FollowingPost.as_view(), name="following_post"),
]
