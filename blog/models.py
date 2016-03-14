from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.conf import settings
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100, unique=True)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateField()
    slug = models.CharField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, primary_key=True, related_name='blog_posts' )
    status = models.CharField(max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    picture = models.ImageField('Blog Images',
                                upload_to='blog_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    # 
    # class Meta:
    #     ordering = ('-publish',)


    def save(self):
        super(Blog, self).save()
        self.slug = '%s' % (
            slugify(self.title)
        )
        super(Blog, self).save()

    def get_absolute_url(self):
        return "/blog/%s/" % self.slug


    def __str__(self):
        return self.title
