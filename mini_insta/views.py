from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Define a view class to show all Instagram Profiles'''
    
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"  # Fixed path
    context_object_name = "profiles"  # Changed to "profiles" for clarity