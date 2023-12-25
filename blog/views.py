from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
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