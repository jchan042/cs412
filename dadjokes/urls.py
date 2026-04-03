# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/31/2026
# Description: Define which views to display for which URLs

from django.urls import path
from .views import *


# maps urls to their respective views
urlpatterns = [
    path('', RandomTemplateView.as_view(), name='random'),
    path('random/', RandomTemplateView.as_view(), name='random'),
    path('jokes/', JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='joke'),
    path('pictures/', PictureListView.as_view(), name='pictures'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='picture'),
    
    # API views
    path('api/', RandomJokeAPIView.as_view()),
    path('api/random/', RandomJokeAPIView.as_view()),
    path('api/jokes/', JokeListAPIView.as_view()),
    path('api/joke/<int:pk>/', JokeDetailAPIView.as_view()),
    path('api/pictures/', PictureListAPIView.as_view()),
    path('api/picture/<int:pk>/', PictureDetailAPIView.as_view()),
    path('api/random_picture/', RandomPictureAPIView.as_view()),
]