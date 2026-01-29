# File: urls.py
# Author: Jocelyn Chan (jchan042@bu.edu) 1/27/2026
# Description: Define which views to display for which URLs
 
from django.urls import path
from django.conf import settings
from . import views
 
from django.conf.urls.static import static    ## add for static files

# Define which views to display for which URLs
urlpatterns = [ 
    path(r'', views.quote, name="quote"), # homepage is same as quote page 
    path(r'quote', views.quote, name="quote"), 
    path(r'show_all', views.show_all, name="show_all"),
    path(r'about', views.about, name="about"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)