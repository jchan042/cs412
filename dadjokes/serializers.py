# File: serializers.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/31/2026
# Description: Convert django data models to a test-representation suitable to transmit over HTTP

from rest_framework import serializers
from .models import *
 
# serializer for the Joke model
class JokeSerializer(serializers.ModelSerializer):
    '''A serializer for the Joke model.'''
 
    class Meta:
        model = Joke
        fields = ['id', 'text', 'author_name', 'timestamp']
 
 
# serializer for the Picture model 
class PictureSerializer(serializers.ModelSerializer):
    '''A serializer for the Picture model.'''
 
    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'author_name', 'timestamp']