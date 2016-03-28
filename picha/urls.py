from django.conf.urls import include, url
from django.contrib import admin

from feedback.views import FeedbackView

urlpatterns = [
    url(r'^$', 'welcome.views.index'),
    url(r'^health$', 'welcome.views.health'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
]
