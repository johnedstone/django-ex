from django.conf.urls import include, url
from django.contrib import admin

from bsub.urls import router
from feedback.views import FeedbackView
from photos.views import PhotoView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', 'welcome.views.index', name='home'),
    url(r'^photos/$', PhotoView.as_view(), name="photos"),
    url(r'^health$', 'welcome.views.health'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^experiences/', include('experiences.urls', namespace='experiences')),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]
