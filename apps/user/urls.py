from django.contrib import admin
from django.urls import path

from apps.user import views
from apps.user.views import Search, UserView, UserLoginView

urlpatterns = [
    path('', UserLoginView.as_view(), name="login"),
    path('signup/', UserView.as_view(), name="signup"),
    path('search/', Search.as_view(), name="search"),
    path('user/', UserView.as_view(), name="user"),
    path('user_list', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),


]
