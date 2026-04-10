# File: serializers.py
# Author: Jocelyn Chan (jchan042@bu.edu) 4/7/2026
# Description: Convert django data models to a test-representation suitable to transmit over HTTP

from rest_framework import serializers
from .models import *

# serializer for the Profile model 
class ProfileSerializer(serializers.ModelSerializer):
    '''A serializer for the Profile model.'''
 
    class Meta:
        model = Profile
        fields = ['id', 'username', 'display_name', 'profile_image_url', 'bio_text', 'join_date']

# serializer for the Post model 
class PostSerializer(serializers.ModelSerializer):
    '''A serializer for the Post model.'''
 
    class Meta:
        model = Post
        fields = ['id', 'profile', 'caption', 'timestamp']

# serializer for the Photo model 
class PhotoSerializer(serializers.ModelSerializer):
    '''A serializer for the Photo model.'''
 
    class Meta:
        model = Photo
        fields = ['id', 'post', 'image_url', 'image_file', 'timestamp']