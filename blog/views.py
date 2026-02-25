from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
from .forms import CreateArticleForm, CreateCommentForm, UpdateArticleForm
from django.urls import reverse
import random

# Create your views here.
class ShowAllView(ListView):
    '''Define a view class to show all blog Articles'''
    
    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles" # plural because many instances
    
    
class ArticleView(DetailView):
    '''Display a single article'''
    
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article" # singular var name
    
    
class RandomArticleView(DetailView):
    '''Display a single article selected at random'''
    
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article" # singular var name
    
    # methods
    def get_object(self):
        '''return one instance of the Article object random'''
        
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        
        return article
    
class CreateArticleView(CreateView):
    '''A view to handle creation of a new Article
    [1] display the HTML form to user (GET)
    [2] process the form submission and store new Article object (POST)'''
    
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"
    
    def form_valid(self, form):
        '''Override the default method to add some debug info'''
        
        # print out the form data:
        print(f'CreateArticleView.form_valid(): {form.cleaned_data}')
        
        # delegate work to the superclass to do the rest:
        return super().form_valid(form)
    
class CreateCommentView(CreateView):
    '''A view to handle creation of a new Comment on an Article'''
    
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"
    
    def get_success_url(self):
        '''Provide a URL to redirect after posting comment'''
        
        pk = self.kwargs['pk']
        return reverse('article', kwargs={'pk':pk})
    
    def get_context_data(self):
        '''Return the dictionary of context vars for use in the templates'''
        
        # calling the superclass method
        context = super().get_context_data()
 
 
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
 
 
        # add this article into the context dictionary:
        context['article'] = article
        return context
    
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Article) to the Comment
        object before saving it to the database.
        '''
 
 
		# instrument our code to display form fields: 
        print(f"CreateCommentView.form_valid: form.cleaned_data={form.cleaned_data}")
        
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # attach this article to the comment
        form.instance.article = article # set the FK
 
 
        # delegate the work to the superclass method form_valid:
        return super().form_valid(form)
    
class UpdateArticleView(UpdateView):
    '''View class to handle update of an article based on its PK'''
    
    model = Article
    form_class = UpdateArticleForm
    template_name = "blog/update_article_form.html"
    
class DeleteCommentView(DeleteView):
    '''View class to delete a comment on an Article'''
    
    model = Comment
    template_name = "blog/delete_comment_form.html"
    
    def get_success_url(self):
        '''Return the URL to redirect to after a successful delete'''
        
        # find the PK for this comment:
        pk = self.kwargs['pk']
        
        # find the comment object:
        comment = Comment.objects.get(pk=pk)
        
        article = comment.article
        
        # return the URL to redirect to:
        return reverse('article', kwargs={'pk': article.pk})