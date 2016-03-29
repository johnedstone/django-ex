from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.ExperienceListView.as_view(),
        name='list',
    ),
    url(
        regex=r'^(?P<slug>[-\w\d]+)-(?P<pk>\d+)/$',
        view=views.ExperienceDetailView.as_view(),
        name="detail",
    ),
)
