from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):   #ListView를 상속 받아서 사용 할거다
    model = Bookmark
    paginate_by = 6
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')