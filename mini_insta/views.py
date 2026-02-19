# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Returns an HTML template view for each URL 

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post

# Create your views here.

# View for all profiles
class ProfileListView(ListView):
    '''Define a view class to show all Instagram Profiles'''
    
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"  # fixed path
    context_object_name = "profiles"  # plural
    
# View for one single profile 
class ProfileDetailView(DetailView):
    '''Define a view class to show a single profile'''
    
    model = Profile 
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile" # singular 
    
# View for the details of one post
class PostDetailView(DetailView):
    '''Define a view class to show the contents of a single post'''
    
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"