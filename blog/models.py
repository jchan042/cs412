from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data of a blog Article by an author'''
    
    # define data attributes with data types
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    # image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True) # an actual image
    
    # string representation
    def __str__(self):
        ''' Return a string representation for this model instance'''
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        '''Return a URL to display one instance of this object'''
        return reverse('article', kwargs={'pk':self.pk})
    
    def get_all_comments(self):
        '''Return a QuerySet of comments about this article'''
        comments = Comment.objects.filter(article=self)
        return comments 
        
class Comment(models.Model):
    '''Encapsulate the idea of a Comment about an Article'''
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Comment'''
        
        return f'{self.text}'
    