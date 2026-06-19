from django.urls import path
from . import views

urlpatterns = [
    path('', views.stating_page, name='stating_page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail_page'),
]
