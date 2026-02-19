from django.contrib import admin

# Register your models here.
from .models import Article, Comment

# give access within Django admin 
admin.site.register(Article)
admin.site.register(Comment)