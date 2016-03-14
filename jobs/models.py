from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class JobCategory(models.Model):
    job_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.job_category_name


class Job(models.Model):
    job_title = models.CharField(max_length=100, unique=True)
    job_vacancy = models.CharField(max_length=100)
    job_description = RichTextField()
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_post_date = models.DateField()
    job_qualification = models.CharField(max_length=100, null=True)
    job_post = models.CharField(max_length=100, null=True)
    job_last_date = models.DateField()
    slug = models.CharField(max_length=150)
    job_logo = models.ImageField('Logo',
                                upload_to='logo_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)

    def save(self):
        super(Job, self).save()
        self.slug = '%s' % (
            slugify(self.job_title)
        )
        super(Job, self).save()

    def get_absolute_url(self):
        return "/jobs/%s/" % self.slug


    def __str__(self):
        return self.job_title
