# File: views.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/31/2026
# Description: Returns an HTML template view for each URL 

import random
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView

from .serializers import JokeSerializer, PictureSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# View for main page with one joke and one picture at random
class RandomTemplateView(TemplateView):
    '''Displays one Joke and one Picture at random'''
    
    template_name = 'dadjokes/random.html'
    
    # pass context variables for the random aspect 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jokes = list(Joke.objects.all()) # all of the jokes
        pictures = list(Picture.objects.all()) # all of the pictures 
        context['joke'] = random.choice(jokes) # selecting a random joke
        context['picture'] = random.choice(pictures) # selecting a random picture
        return context
    
    
# View for showing a page with all jokes 
class JokeListView(ListView):
    '''Shows a page with all jokes but no images'''
    
    template_name = 'dadjokes/jokes.html'
    model = Joke
    context_object_name = 'jokes' # plural
    
    
# View for showing one Joke via PK 
class JokeDetailView(DetailView):
    '''Show one Joke by its PK'''
    
    template_name = 'dadjokes/joke.html'
    model = Joke
    context_object_name = 'joke' # singular
    
    
# View for showing a page with all pictures 
class PictureListView(ListView):
    '''Shows a page with all pictures but no jokes'''
    
    template_name = 'dadjokes/pictures.html'
    model = Picture
    context_object_name = 'pictures' # plural

# View for showing one Picture via PK 
class PictureDetailView(DetailView):
    '''Show one image by its PK'''
    
    template_name = 'dadjokes/picture.html'
    model = Picture
    context_object_name = 'picture' # singular
    
# API VIEWS #

# returns one joke at random
class RandomJokeAPIView(APIView):
    '''GET method: returns one Joke selected at random'''
 
    def get(self, request):
        jokes = list(Joke.objects.all())
        joke = random.choice(jokes) if jokes else None
        serializer = JokeSerializer(joke)
        return Response(serializer.data)
 
 
# returns all jokes and create a new joke
class JokeListAPIView(generics.ListCreateAPIView):
    '''GET method: returns all Jokes. POST method: creates a new Joke.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
 
 
# reutrns one joke by PK
class JokeDetailAPIView(generics.RetrieveAPIView):
    '''GET method: returns one Joke by PK'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
 
 
# reutrns all pictures 
class PictureListAPIView(generics.ListAPIView):
    '''GET method: returns all Pictures'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
 
 
# return one picture by PK
class PictureDetailAPIView(generics.RetrieveAPIView):
    '''GET method: returns one Picture by PK '''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
 

# return one picture at random
class RandomPictureAPIView(APIView):
    '''GET method: returns one Picture selected at random'''
 
    def get(self, request):
        pictures = list(Picture.objects.all())
        picture = random.choice(pictures) if pictures else None
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    
