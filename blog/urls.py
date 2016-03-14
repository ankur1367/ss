from django.conf.urls import url

from . import views
from .views import BlogListView, BlogDetailView

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name='blog-detail'),
]
