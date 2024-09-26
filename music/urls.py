from django.urls import path
from .views import *

urlpatterns = [
    path('songs/', list, name='list'),
    path('songs/upload/', upload, name='upload'),
    path('songs/<int:pk>/', detail, name='detail'),
    path('songs/<int:pk>/update/', update, name='update'),
    path('songs/<int:pk>/delete/', delete, name='delete'),
]
