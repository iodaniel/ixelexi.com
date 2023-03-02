from django.shortcuts import render

# Create your views here.
from django.views import generic 

from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('create_at')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'