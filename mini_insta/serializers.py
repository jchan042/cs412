# File: serializers.py
# Author: Jocelyn Chan (jchan042@bu.edu) 4/7/2026
# Description: Convert django data models to a test-representation suitable to transmit over HTTP

from rest_framework import serializers
from .models import *

# File: serializers.py
# Author: Jocelyn Chan (jchan042@bu.edu) 4/7/2026
# Description: Convert django data models to a text representation suitable to transmit over HTTP


class ProfileSerializer(serializers.ModelSerializer):
    '''A serializer for the Profile model.'''

    class Meta:
        model = Profile
        fields = ['id', 'username', 'display_name', 'profile_image_url', 'bio_text', 'join_date']


class PhotoSerializer(serializers.ModelSerializer):
    '''A serializer for the Photo model.'''

    resolved_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['id', 'post', 'image_url', 'image_file', 'resolved_image_url', 'timestamp']

    def get_resolved_image_url(self, obj):
        '''
        Return the actual usable image URL for this photo.
        Prefer uploaded image_file if present; otherwise use image_url.
        '''
        return obj.get_image_url()


class PostSerializer(serializers.ModelSerializer):
    '''A serializer for the Post model.'''

    preview_image_url = serializers.SerializerMethodField()
    username = serializers.CharField(source='profile.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'profile', 'username', 'caption', 'timestamp', 'preview_image_url']

    def get_preview_image_url(self, obj):
        first_photo = obj.get_all_photos().first()
        if not first_photo:
            return None
        return first_photo.get_image_url()


class PostDetailSerializer(serializers.ModelSerializer):
    '''
    A detailed serializer for a single Post, including all photos attached to it.
    '''
    photos = PhotoSerializer(source='get_all_photos', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'profile', 'caption', 'timestamp', 'photos']