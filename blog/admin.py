from django.contrib import admin

# Register your models here.
from .models import Article

# give access within Django admin 
admin.site.register(Article)