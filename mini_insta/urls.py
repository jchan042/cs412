# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Define which views to display for which URLs

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    # public views
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="profile"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post"),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name="followers"),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name="following"),

    # post update/delete 
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name="update_post"),

    # authenticated views 
    path('profile', ShowOwnProfileView.as_view(), name="own_profile"),
    path('profile/feed', PostFeedListView.as_view(), name="feed"),
    path('profile/search', SearchView.as_view(), name="search"),
    path('profile/update', UpdateProfileView.as_view(), name="update"),
    path('profile/create_post', CreatePostView.as_view(), name="create_post"),

    # registration
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),

    # login/logout 
    path('login/', auth_views.LoginView.as_view(template_name='mini_insta/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout_confirmation'), name="logout"),
    path('logout_confirmation/', LogoutConfirmationView.as_view(), name="logout_confirmation"),

    # follow/unfollow
    path('profile/<int:pk>/follow', FollowProfileView.as_view(), name="follow"),
    path('profile/<int:pk>/delete_follow', UnfollowProfileView.as_view(), name="delete_follow"),

    # like/unlike
    path('post/<int:pk>/like', LikePostView.as_view(), name="like"),
    path('post/<int:pk>/delete_like', UnlikePostView.as_view(), name="delete_like"),
        
    # API auth
    path('api/login/', LoginAPIView.as_view(), name="api_login"),

    # API views
    path('api/profiles/', ProfileListAPIView.as_view(), name="profiles_view"),
    path('api/profiles/<int:pk>/', ProfileAPIView.as_view(), name="profile_view"),
    path('api/profiles/<int:pk>/posts/', ProfilePostsAPIView.as_view(), name="profile_posts_view"),
    path('api/profiles/<int:pk>/feed/', FeedAPIView.as_view(), name="feed_view"),
    path('api/profiles/<int:pk>/posts/create/', MakePostAPIView.as_view(), name="make_post_view"),

    # API endpoints for post detail + photos
    path('api/profiles/<int:pk>/posts/<int:post_pk>/', PostDetailAPIView.as_view(), name="post_detail_view"),
    path('api/profiles/<int:pk>/posts/<int:post_pk>/photos/', PostPhotosAPIView.as_view(), name="post_photos_view"),
    path('api/profiles/<int:pk>/posts/<int:post_pk>/photos/create/', MakePhotoAPIView.as_view(), name="make_photo_view"),
]