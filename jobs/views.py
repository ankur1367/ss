from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import Job




class JobListView(ListView):

    model = Job

    def get_context_data(self, **kwargs):
        latest_job_list = Job.objects.order_by('-post_date')[:5]
        context = super(JobListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class JobDetailView(DetailView):

    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
