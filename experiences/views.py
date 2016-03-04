from django.views.generic import DetailView, ListView
from .models import Experience

class ExperienceListView(ListView):

    model = Experience

class ExperienceDetailView(DetailView):

    model = Experience
