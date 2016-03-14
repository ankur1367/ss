from django.conf.urls import url

from . import views
from .views import JobListView, JobDetailView

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', JobDetailView.as_view(), name='job-detail'),
]
