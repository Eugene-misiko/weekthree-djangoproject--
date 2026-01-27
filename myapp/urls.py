from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, follow_user, unfollow_user,user_search_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profile/<int:user_id>/follow/', follow_user, name='follow'),
    path('profile/<int:user_id>/unfollow/', unfollow_user, name='unfollow'),
    path('search/', user_search_view, name='user_search'),    
]
