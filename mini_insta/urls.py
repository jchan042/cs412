# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Define which views to display for which URLs

from django.urls import path
from .views import ProfileListView  # hardcoding importing all the views 

urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all_profiles', ProfileListView.as_view(), name="show_all_profiles"),
]