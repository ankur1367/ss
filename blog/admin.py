from django.contrib import admin
from .models import Blog, Category
from ckeditor.widgets import CKEditorWidget
# Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     pass
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
