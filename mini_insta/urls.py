# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Define which views to display for which URLs

from django.urls import path
from .views import ShowAllProfilesView  # Fixed import

urlpatterns = [
    path('show_all', ShowAllProfilesView.as_view(), name="show_all"),
]