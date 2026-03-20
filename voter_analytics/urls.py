# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/18/2026
# Description: Define which views to display for which URLs

from django.urls import path
from .views import *


# maps urls to their respective views
urlpatterns = [
    path('', VotersListView.as_view(), name='voters'),
    path('voters/', VotersListView.as_view(), name='voters'),
    path('voter/<int:pk>/', VoterDetailView.as_view(), name='voter'),
    path('graphs/', GraphsListView.as_view(), name='graphs'),
]