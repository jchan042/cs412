# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Returns an HTML template view for each URL 

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm

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
    
# View for creating a new Post
class CreatePostView(CreateView):
    '''Define a view class to handle creating a new post'''
    
    model = Post
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"
    
    def get_context_data(self, **kwargs):
        '''Add the profile to the context so the template can use it'''
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''Attach the profile and photo before saving the post'''
        # find the profile using the pk from the URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # attach the profile to the post
        form.instance.profile = profile
        # save the post
        post = form.save()
        # create the photo using the image_url from the form
        image_url = self.request.POST.get('image_url')
        if image_url:
            Photo.objects.create(post=post, image_url=image_url)
        return super().form_valid(form)