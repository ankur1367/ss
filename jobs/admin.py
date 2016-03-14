from django.contrib import admin
from .models import Job, JobCategory
from ckeditor.widgets import CKEditorWidget
# Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     pass
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("job_title",)}

admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory)
