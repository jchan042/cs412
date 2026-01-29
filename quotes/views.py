# File: views.py
# Author: Jocelyn Chan (jchan042@bu.edu) 1/27/2026
# Description: view page for the quotes app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


import time
import random

# Global scope with list of quotes and images with 3 each
quotes = ["Please don't look back because you did your best and you'll be the only one who can protect yourself.",
          "Happiness is not something you have to achieve, you can still feel happy during the process of achieving something.",
          "Life is a sculpture that you cast as you make mistakes and learn from them."]

images = ["https://koreajoongangdaily.joins.com/data/photo/2023/03/15/d0b38ba5-9daf-47b2-b35e-a3835f384483.jpg",
          "https://st1.bollywoodlife.com/wp-content/uploads/2021/08/kim-namjoonnn.png?impolicy=Medium_Widthonly&w=412&h=290",
          "https://img.global.news.samsung.com/global/wp-content/uploads/2025/06/Samsung-TVs-and-Displays-Samsung-Art-TV-Samsung-Art-Store-Art-Basel-in-Basel-BTS-of-RM-Becomes-Global-Ambassador_main1.jpg"]

# View for quote/main page 
def quote(request):
    """View for homepage"""

    # delegate work to quote.html template for display
    template = 'quotes/quote.html'
    
    # generate random image and quote using context vars
    context = {
        'random_quote': random.choice(quotes),
        'random_image': random.choice(images),

    }
    
    return render(request, template, context)
    
# View page for showing all quotes and images     
def show_all(request): 
    """View for show all page"""
    
    # delegate work to show_all.html template for display
    template = 'quotes/show_all.html'
    
    # context variables for showing all quotes and images
    context = {
        'all_quotes': quotes,
        'all_images': images,
    }
    
    return render(request, template, context)
    
    
    
# View page for the about page that displays the info of the person 
def about(request):
    """Define a view to show the 'about.html template."""
 
    # delegate work to about.html template for display
    template = 'quotes/about.html' 
 
    return render(request, template)