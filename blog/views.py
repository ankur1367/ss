from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import Blog
class BlogListView(ListView):

    model = Blog

    def get_context_data(self, **kwargs):
        latest_blog_list = Blog.objects.order_by('-post_date')[:5]
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
