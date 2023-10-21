from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Add new article',
    }


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'My Store TechBlog'
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'View blog article'
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Edit article',
    }


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Delete article',
    }

