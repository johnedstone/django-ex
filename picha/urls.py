from django.conf.urls import include, url
from django.contrib import admin

from photos.views import PhotoView
from feedback.views import FeedbackView

urlpatterns = [
    url(r'^$', 'welcome.views.index', name='home'),
    url(r'^photos/$', PhotoView.as_view(), name="photos"),
    url(r'^health$', 'welcome.views.health'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^experiences/', include('experiences.urls', namespace='experiences')),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
]
