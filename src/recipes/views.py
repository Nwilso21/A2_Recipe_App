from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   return render(request, 'recipes/recipes_home.html')


class recipeListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class recipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'

def success(request):
    return render(request, 'recipes/success.html')