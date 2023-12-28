from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
class HomePageView(ListView):
    model = BlogPost
    template_name = "home.html"
    context_object_name = "post_list"

class DetailPageView(DetailView):
    model = BlogPost
    template_name = "blog_details.html"
    context_object_name = "post"

class PostNewView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title','author','body' ]

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'update_post.html'
    fields = ['title', 'body']

class DeletPostView(DeleteView):
    model = BlogPost
    template_name = 'del_post.html'
    success_url = reverse_lazy("home")
    
