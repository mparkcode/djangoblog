from django.urls import path
from .views import get_posts, post_detail, new_post, edit_post

urlpatterns = [
    path('new', new_post, name="new_post"),
    path('<int:pk>/edit', edit_post, name="edit_post"),
    path('<int:pk>/', post_detail, name="post_detail"),
    path('', get_posts, name="get_posts"), 
]