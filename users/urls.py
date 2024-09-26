from django.urls import path
from .views import (
    user_list,
    user_create,
    user_detail,
    user_update,
    user_delete,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', user_list, name='userlist'),
    path('users/create/', user_create, name='usercreate'),
    path('users/<uuid:pk>/', user_detail, name='userdetail'),
    path('users/<uuid:pk>/update/', user_update, name='userupdate'),
    path('users/<uuid:pk>/delete/', user_delete, name='userdelete'),
]