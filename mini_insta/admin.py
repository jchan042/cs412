# File: admin.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/10/2026
# Description: Used to define the DB structure/schema

from django.contrib import admin
# import the models first
from .models import Profile, Post, Photo

# register the models into the admin
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)