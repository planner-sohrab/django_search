from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City
from django.db.models import Q

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name='search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
            Q(name__icontains= query) | Q(state__icontains=query)
         ) 
        return object_list