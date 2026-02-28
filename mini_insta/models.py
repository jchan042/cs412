# File: models.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/10/2026
# Description: Used to define the DB structure/schema

from django.db import models
from django.urls import reverse

# Create your models here.

# Profile model for a user's profile 
class Profile(models.Model): 
    '''Encapsulate the data of an Insta Profile'''
    
    # all the attributes of the profile model
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)
    
    # implement string representation
    def __str__(self):
        '''Return a string representation for this model instance'''
        return f'{self.username} profile'    
    
    # accessor method to find and return all posts for a given profile 
    def get_all_posts(self):
        '''Return a QuerySet of posts about this profile'''
    
        return Post.objects.filter(profile=self).order_by('timestamp')
    
    # redirect user to this URL 
    def get_absolute_url(self):
        '''Return the URL to display this profile'''
        return reverse('profile', kwargs={'pk': self.pk})
    
# Post model for a user's profile 
class Post(models.Model):
    '''Encapsulate the data of a person's Instagram post'''
    
    # all the attributes of the post model
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)
    
    # implement string representation
    def __str__(self):
        '''Return a string representation for this model instance'''
        return f'{self.profile} post {self.pk}'
    
    # accessor method to find and return all photos for a given post 
    def get_all_photos(self):
        '''Return a QuerySet of photos about this post'''
        return Photo.objects.filter(post=self).order_by('timestamp')
    
    # accessor methond to find and return the correct url for the post
    def get_absolute_url(self):
        '''Return the URL to display this post'''
        return reverse('post', kwargs={'pk': self.pk})
    
class Photo(models.Model):
    '''Encapsulate the data of an Insta Photo for a post'''
    
    # all the attributes of the post model
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)
    
    # implement string representation
    def __str__(self):
        '''Return a string representation for this model instance'''
        return f'{self.post.profile} post {self.post.pk} photo {self.pk} - {self.get_image_url()}'
    
    # accessor method to return the URL for an image
    def get_image_url(self): 
        '''Return the URL for an image'''
        
        # conditional to see if the image url attribute exists 
        if self.image_file:
            return self.image_file.url
        return self.image_url