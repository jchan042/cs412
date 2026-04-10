# File: views.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: Returns an HTML template view for each URL 

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Profile, Post, Photo, Follow, Like
from .forms import CreatePostForm, UpdateProfileForm, CreateProfileForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# import API 
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# mixin: get logged in user's profile 
# subclass of loginrequiredmixin
class ProfileLoginRequiredMixin(LoginRequiredMixin):
    '''Extends LoginRequiredMixin with a helper to get the logged in user's Profile'''
    
    def get_login_url(self):
        '''Return the URL for this app's login page'''
        return reverse('login')
    
    def get_user_profile(self):
        '''Return the Profile associated with the currently logged in User or None'''
        return Profile.objects.filter(user=self.request.user).first()


# no login required for the below views 

# View for all profiles
class ProfileListView(ListView):
    '''Define a view class to show all Instagram Profiles'''
    
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"  # fixed path
    context_object_name = "profiles"  # plural

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the logged-in user's profile so base.html nav works if logged in
        if self.request.user.is_authenticated:
            context['profile'] = Profile.objects.filter(user=self.request.user).first()
        return context

    
# View for one single profile 
class ProfileDetailView(DetailView):
    '''Define a view class to show a single profile'''
    
    model = Profile 
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"  # singular (pf being viewed)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the logged-in user's own profile separately for the nav
        if self.request.user.is_authenticated:
            user_profile = Profile.objects.filter(user=self.request.user).first()
            context['user_profile'] = user_profile
            # check if the logged-in user already follows this profile
            viewed_profile = self.get_object()
            if user_profile and user_profile != viewed_profile:
                context['is_following'] = Follow.objects.filter(
                    follower_profile=user_profile, profile=viewed_profile
                ).exists()
        return context

    
# View for the details of one post
class PostDetailView(DetailView):
    '''Define a view class to show the contents of a single post'''
    
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_profile = Profile.objects.filter(user=self.request.user).first()
            context['profile'] = user_profile
            # check if the logged-in user already liked this post
            post = self.get_object()
            if user_profile:
                context['has_liked'] = Like.objects.filter(
                    profile=user_profile, post=post
                ).exists()
        return context

    
# View for showing a profile's followers
class ShowFollowersDetailView(DetailView):
    '''Define a view class to show all followers of a profile'''
    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


# View for showing who a profile is following
class ShowFollowingDetailView(DetailView):
    '''Define a view class to show all profiles that a profile follows'''
    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


# login required for the below views 

# View for creating a new Post (pk removed from URL — uses logged-in user's profile)
class CreatePostView(ProfileLoginRequiredMixin, CreateView):
    '''Define a view class to handle creating a new post'''
    
    model = Post
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"
    
    def get_context_data(self, **kwargs):
        '''Add the profile to the context so the template can use it'''
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_user_profile()
        return context
    
    def form_valid(self, form):
        '''Attach the profile and photo before saving the post'''
        # find the profile for the logged-in user
        profile = self.get_user_profile()
        # attach the profile to the post
        form.instance.profile = profile
        # save the post
        post = form.save()
        
        # read data for files
        files = self.request.FILES.getlist('upload-photos')
        
        # loop through each file and create a Photo object
        for file in files:
            Photo.objects.create(post=post, image_file=file)
            
        return super().form_valid(form)

        # create the photo using the image_url from the form
        # image_url = self.request.POST.get('image_url')
        # if image_url:
        #     Photo.objects.create(post=post, image_url=image_url)


# View for updating a user's profile 
class UpdateProfileView(ProfileLoginRequiredMixin, UpdateView):
    '''Define a view class to handle updating the logged-in user's profile'''
    model = Profile 
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def get_object(self):
        '''Return the Profile of the logged-in user instead of using URL pk'''
        return self.get_user_profile()
    
    def get_context_data(self, **kwargs):
        '''Add the profile to the context so the template can use it'''
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_user_profile()
        return context


# View for deleting a post
class DeletePostView(ProfileLoginRequiredMixin, DeleteView):
    '''Define a view class to handle deleting a post'''
    
    model = Post
    template_name = "mini_insta/delete_post_form.html"
    
    def get_context_data(self, **kwargs):
        '''Add the post and profile to the context so the template can use them'''
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        context['post'] = post
        context['profile'] = self.get_user_profile()
        return context
    
    def get_success_url(self):
        '''Redirect to the profile page after a successful delete'''
        return reverse('profile', kwargs={'pk': self.get_user_profile().pk})


# View for updating a post
class UpdatePostView(ProfileLoginRequiredMixin, UpdateView):
    '''Define a view class to handle updating a post caption'''
    model = Post
    fields = ['caption']
    template_name = "mini_insta/update_post_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        context['post'] = post
        context['profile'] = self.get_user_profile()
        return context


# View for the post feed (login required)
class PostFeedListView(ProfileLoginRequiredMixin, ListView):
    '''Define a view class to show the post feed for a profile'''
    model = Post
    template_name = "mini_insta/show_feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        '''Return the post feed for the logged-in user's profile, or empty if no profile'''
        profile = self.get_user_profile()
        # if the logged-in user has no profile yet, return an empty queryset
        if profile is None:
            return Post.objects.none()
        return profile.get_post_feed()

    def get_context_data(self, **kwargs):
        '''Add the profile to the context'''
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_user_profile()
        return context


# View for searching profiles and posts (login required)
class SearchView(ProfileLoginRequiredMixin, ListView):
    '''Define a view class to handle searching profiles and posts'''
    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profiles"

    def dispatch(self, request, *args, **kwargs):
        '''If no query is present, show the search form; otherwise process results'''
        # if no query in the GET params render the search form template directly
        if 'query' not in request.GET:
            profile = Profile.objects.filter(user=request.user).first()
            return render(request, 'mini_insta/search.html', {'profile': profile, 'query': ''})
        # let the ListView handle it normally
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''Return profiles matching the search query'''
        query = self.request.GET.get('query', '')
        if query:
            return (Profile.objects.filter(username__icontains=query) | 
                    Profile.objects.filter(display_name__icontains=query) |
                    Profile.objects.filter(bio_text__icontains=query))
        return Profile.objects.none()

    def get_context_data(self, **kwargs):
        '''Add profile, query, and matching posts to context'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        context['profile'] = self.get_user_profile()
        context['query'] = query
        if query:
            context['posts'] = Post.objects.filter(caption__icontains=query)
        else:
            context['posts'] = Post.objects.none()
        return context


# View for showing the logged-in user's own profile page
class ShowOwnProfileView(ProfileLoginRequiredMixin, DetailView):
    '''Define a view class to show the logged-in user their own profile'''
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        '''Return the Profile of the logged-in user instead of using URL pk'''
        return self.get_user_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # view own profile
        context['user_profile'] = self.get_user_profile()
        return context


# View for creating a new Profile + a Django User account
class CreateProfileView(CreateView):
    '''Define a view class to handle creating a new Profile and User together'''
    
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

    def get_context_data(self, **kwargs):
        '''Add the UserCreationForm to the context alongside the CreateProfileForm'''
        context = super().get_context_data(**kwargs)
        # include the django user creation form so the template can display it
        context['user_creation_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        '''Create the User, log them in, attach to the Profile, then save'''
        # reconstruct the UserCreationForm from POST data
        user_creation_form = UserCreationForm(self.request.POST)
        
        # save the new User object
        user = user_creation_form.save()
        
        # log the new user in automatically
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        
        # attach the new User to the Profile instance before saving
        form.instance.user = user
        
        # set the username field on the Profile from the User's username
        form.instance.username = user.username
        
        # delegate the rest to the superclass
        return super().form_valid(form)


# View for the logged-out confirmation page
class LogoutConfirmationView(TemplateView):
    '''Define a view class to show a logout confirmation page'''
    template_name = "mini_insta/logged_out.html"


# View for following another profile
class FollowProfileView(ProfileLoginRequiredMixin, TemplateView):
    '''Define a view to handle following another Profile'''
    template_name = "mini_insta/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Create a Follow relationship then redirect back to the followed profile'''
        # get the logged-in user's profile
        user_profile = Profile.objects.filter(user=request.user).first()
        # get the profile to follow using the URL pk
        other_profile = Profile.objects.get(pk=self.kwargs['pk'])
        
        # only create a follow if not already following and not self-follow
        if user_profile and user_profile != other_profile:
            Follow.objects.get_or_create(profile=other_profile, follower_profile=user_profile)
        
        # redirect back to the profile page that was followed
        return redirect(reverse('profile', kwargs={'pk': other_profile.pk}))


# View for unfollowing a profile
class UnfollowProfileView(ProfileLoginRequiredMixin, TemplateView):
    '''Define a view to handle unfollowing a Profile'''
    template_name = "mini_insta/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Delete the Follow relationship then redirect back to the unfollowed profile'''
        # get the logged-in user's profile
        user_profile = Profile.objects.filter(user=request.user).first()
        # get the profile to unfollow using the URL pk
        other_profile = Profile.objects.get(pk=self.kwargs['pk'])
        
        # delete the follow relationship if it exists
        Follow.objects.filter(profile=other_profile, follower_profile=user_profile).delete()
        
        # redirect back to the profile page that was unfollowed
        return redirect(reverse('profile', kwargs={'pk': other_profile.pk}))


# View for liking a post
class LikePostView(ProfileLoginRequiredMixin, TemplateView):
    '''Define a view to handle liking a Post'''
    template_name = "mini_insta/show_post.html"

    def dispatch(self, request, *args, **kwargs):
        '''Create a Like then redirect back to the post'''
        # get the logged-in user's profile
        user_profile = Profile.objects.filter(user=request.user).first()
        # get the post to like using the URL pk
        post = Post.objects.get(pk=self.kwargs['pk'])
        
        # only allow liking posts that belong to a different profile
        if user_profile and user_profile != post.profile:
            Like.objects.get_or_create(post=post, profile=user_profile)
        
        # redirect back to the post page
        return redirect(reverse('post', kwargs={'pk': post.pk}))


# View for unliking a post 
class UnlikePostView(ProfileLoginRequiredMixin, TemplateView):
    '''Define a view to handle unliking a Post'''
    template_name = "mini_insta/show_post.html"

    def dispatch(self, request, *args, **kwargs):
        '''Delete the Like then redirect back to the post'''
        # get the logged-in user's profile
        user_profile = Profile.objects.filter(user=request.user).first()
        # get the post to unlike using the URL pk
        post = Post.objects.get(pk=self.kwargs['pk'])
        
        # delete the like if it exists
        Like.objects.filter(post=post, profile=user_profile).delete()
        
        # redirect back to the post page
        return redirect(reverse('post', kwargs={'pk': post.pk}))
    
    
# API VIEWS #

# returns one profile
class ProfileAPIView(generics.RetrieveAPIView):
    '''GET method that returns one Profile'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
 
 
# returns a list of profiles
class ProfileListAPIView(generics.ListAPIView):
    '''GET method that returns a list of Profile objects'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
 
 
# returns all posts for one profile
class ProfilePostsAPIView(generics.ListAPIView):
    '''GET method that returns all Posts for a given Profile'''
    serializer_class = PostSerializer
 
    def get_queryset(self):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile.get_all_posts()
 
 
# returns a feed for one profile
class FeedAPIView(generics.ListAPIView):
    '''GET method that returns the feed of Posts from profiles that a given Profile follows'''
    serializer_class = PostSerializer
 
    def get_queryset(self):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile.get_post_feed()
 
 
# creating a post
class MakePostAPIView(generics.CreateAPIView):
    '''POST method that creates a new Post for a given Profile'''
    serializer_class = PostSerializer
 
    def perform_create(self, serializer):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        serializer.save(profile=profile)