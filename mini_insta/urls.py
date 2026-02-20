# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Define which views to display for which URLs

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView  # hardcoding importing all the views 

# Routes URLs to display their respective view
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="profile"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post"),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name="create_post"),
]
