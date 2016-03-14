from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import allauth
import profiles.urls
import blog.urls
import accounts.urls
import jobs.urls
import quiz.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^blog/', include(blog.urls, namespace='blog')),
    url(r'^jobs/', include(jobs.urls, namespace='job')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quiz/', include(quiz.urls, namespace='job')),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^accounts/', include('allauth.urls')),
    # (r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
