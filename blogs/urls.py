from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
]
