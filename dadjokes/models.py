# File: models.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/31/2026
# Description: Used to define the DB structure/schema


from django.db import models

# Create your models here.

# Joke model 
class Joke(models.Model): 
    '''Store the text of a joke, the name and timestamp'''
    
    # fields for the model
    text = models.TextField()
    author_name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Joke #{self.pk} by {self.author_name}"
    
    
# Picture model
class Picture(models.Model):
    '''Store the image url of an image, name and timestamp'''
    
    # fields for the picture model
    image_url = models.URLField(blank=True)
    author_name = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Picture #{self.pk} by {self.author_name}"
    
    