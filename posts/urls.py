from django.urls import path
from .views import feed_view, create_post_view, post_detail_view, like_post_view,add_comment_view

urlpatterns = [
    path('', feed_view, name='feed'),
    path('create/', create_post_view, name='create_post'),
    path('<int:post_id>/', post_detail_view, name='post_detail'),
    path('<int:post_id>/like/', like_post_view, name='like_post'),
    path('<int:post_id>/comment/', add_comment_view, name='add_comment'),
]