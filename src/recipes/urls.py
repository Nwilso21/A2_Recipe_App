from django.urls import path
from .views import home
from .views import recipeListView, recipeDetailView

app_name = 'recipes'  

urlpatterns = [
   path('', home, name = 'home'),
   path('list/', recipeListView.as_view(), name='list'),
   path('list/<pk>', recipeDetailView.as_view(), name='detail'),
]

