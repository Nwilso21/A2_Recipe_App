from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart

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



def search(request):
   form = RecipesSearchForm(request.POST or None)
   default='Hard'
   default_qs=Recipes.objects.filter(difficulty=default)
   recipes_df=pd.DataFrame(default_qs.values())
   chart = None
   if request.method =='POST':
       recipe_difficulty = request.POST.get('recipe_difficulty')
       chart_type = request.POST.get('chart_type')

       qs =Recipes.objects.filter(difficulty=recipe_difficulty)
       print(qs)
    
       if qs:      #if data found
           #convert the queryset values to pandas dataframe
           recipes_df=pd.DataFrame(qs.values()) 
           chart=get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
           print(recipes_df)

       print (recipe_difficulty, chart_type)
   context={
           'form': form,
           'recipes_df': recipes_df.to_html(),
           'chart' : chart
   }

   return render(request, 'recipes/search.html', context)