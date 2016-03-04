from django.contrib import admin
from .models import Experience

class ExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Experience, ExperienceAdmin)
