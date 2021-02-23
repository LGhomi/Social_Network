from django.contrib import admin
from django.urls import path

from apps.user.views import Search, UserView

urlpatterns = [
    path('search/', Search.as_view(), name="search"),
    path('user/', UserView.as_view(), name="user"),
]
