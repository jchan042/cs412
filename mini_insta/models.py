# File: models.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/10/2026
# Description: Used to define the DB structure/schema

from django.db import models

# Create your models here.

# Profile model for a user's profile 
class Profile(models.Model): 
    '''Encapsulate the data of an Insta Profile'''
    
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)
    
    # implement string represent 
    def __str__(self):
        '''Return a string representation for this model instance'''
        return f'{self.username} profile'      