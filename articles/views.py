from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.exceptions import PermissionDenied # new
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView): 
  model = Article
  template_name = 'article_list.html'
  login_url = 'login' 


class ArticleDetailView(LoginRequiredMixin, DetailView): # new 
  model = Article
  template_name = 'article_detail.html'
  login_url = 'login' # new


class ArticleUpdateView(LoginRequiredMixin, UpdateView): # new 
  model = Article
  fields = ('title', 'body',)
  template_name = 'article_edit.html'
  login_url = 'login' # new
  
  def dispatch(self, request, *args, **kwargs): # new 
    obj = self.get_object()
    if obj.author != self.request.user:
      raise PermissionDenied
    return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login' # new
    
    def dispatch(self, request, *args, **kwargs): # new 
      obj = self.get_object()
      if obj.author != self.request.user:
        raise PermissionDenied
      return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView): 
  model = Article
  template_name = 'article_new.html'
  fields = ('title', 'body')
  login_url = 'login' 
  
  
  def form_valid(self, form): # new 
      form.instance.author = self.request.user 
      return super().form_valid(form)
  
