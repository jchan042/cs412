# File: admin.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/10/2026
# Description: Used to define the DB structure/schema

from django.contrib import admin

# Register your models here.

# register profile model
from .models import Profile
admin.site.register(Profile)