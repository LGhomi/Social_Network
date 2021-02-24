from django.urls import path

from apps.post.views import PostView, PostList, PostDetail, PagedPostList

urlpatterns = [
    path('', PostList.as_view(), name="posts"),
    path('<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('add_post/', PostView.as_view(), name="add_new_post"),
    path('paged_post_list/', PagedPostList.as_view(), name='paged_post_list'),
]
