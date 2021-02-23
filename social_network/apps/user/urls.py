from django.contrib import admin
from django.urls import path

from social_network.apps.user.views import UserLoginView, Search, UserView

urlpatterns = [
    path('search/', Search.as_view(), name="search"),
    path('user/', UserView.as_view(), name="user"),
    path('login/', UserLoginView.as_view(), name="login"),
]
