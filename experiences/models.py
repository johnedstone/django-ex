from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify as django_slugify
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField


@python_2_unicode_compatible
class Experience(models.Model):
    title = models.CharField(max_length=200)
    experience = models.TextField()
    publish = models.BooleanField(default=True, blank=False)
    slug = AutoSlugField(populate_from=lambda instance: instance.title, slugify=django_slugify, editable=True,)

    # objects = models.Manager()
    # published_experiences = PublishedExperiences()

    class Meta:
        ordering = ['-title',]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     '''http://www.wellfireinteractive.com/blog/fast-and-beautiful-urls-with-django/'''
    #     return reverse('experiences:detail', kwargs={"slug": self.slug, "pk": self.pk})

