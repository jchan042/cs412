from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data of a blog Article by an author'''
    
    # define data attributes with data types
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)
    
    # string representation
    def __str__(self):
        ''' Return a string representation fo this model instance'''
        return f'{self.title} by {self.author}'
        