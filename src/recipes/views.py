from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes

# Create your views here.

def home(request):
   return render(request, 'recipes/recipes_home.html')

class recipeListView(ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class recipeDetailView(DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'