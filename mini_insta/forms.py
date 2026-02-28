# File: forms.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/12/2026
# Description: The form to create a post 

from django import forms
from .models import *

# Form to create a post
class CreatePostForm(forms.ModelForm):
    '''A form to add a Post to the database'''
    
    class Meta:
        '''Associate this form with a Post model from our db'''
        
        model = Post
        fields = ['caption']
        
# Form to update a profile 
class UpdateProfileForm(forms.ModelForm):
    '''A form to change and update an existing profile'''
    
    class Meta:
        '''Associate this form with a Profile model from our DB'''
        
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']