from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page


class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
