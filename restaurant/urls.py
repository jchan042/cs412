# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/3/2026
# Description: Define which views to display for which urls

from django.urls import path
from django.conf import settings
from . import views
# URL patterns for this app:
urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'main/', views.main, name='main'),
    path(r'order/', views.order, name='order'),
    path(r'confirmation/', views.confirmation, name='confirmation'),
]