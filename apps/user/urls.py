from django.contrib import admin
from django.urls import path, include

from apps.user import views
from apps.user.views import Search, UserView, UserLoginView, LogoutView, UserName,followers_list,following_list

urlpatterns = [
    path('', UserLoginView.as_view(), name="login"),
    path('signup/', UserView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('My_follower/', followers_list.as_view(), name="my_follower"),
    path('My_following/', following_list.as_view(), name="my_following"),
    path('search/', Search.as_view(), name="search"),
    path('user/', UserView.as_view(), name="user"),
    path('user_list', views.UserList.as_view(), name='user_list'),
    # path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('profile/', views.UserName.as_view(), name='profile'),
    path('<int:pk>/', include([
        path('', views.UserDetail.as_view(), name='user_detail'),
        path('follow/', views.follow, name='follow')
    ]

    ), )
]
