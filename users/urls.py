from django.urls import path
from .views import UserCreateView,UserListView

urlpatterns = [
    path('add/',UserCreateView.as_view(),name='user-add'),
    path('list/',UserListView.as_view(),name='user-list'),
]
