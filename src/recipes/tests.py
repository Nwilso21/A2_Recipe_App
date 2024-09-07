from django.test import TestCase
from .models import Recipes

# Create your tests here.

class RecipeModelTest(TestCase):
    
    def setUpTestData():
        Recipes.objects.create(recipe_id=1,name="Soup",cooking_time=10,ingredients="Noodles,Broth,Chicken,Carrots",difficulty="intermediate")

    def test_recipe_name(self):
       Recipe = Recipes.objects.get(recipe_id=1)

       field_label = Recipe._meta.get_field('name').verbose_name

       self.assertEqual(field_label, 'name')

    def test_recipe_ingredients(self):
        Recipe = Recipes.objects.get(recipe_id=1)

        max_length = Recipe._meta.get_field('ingredients').max_length

        self.assertEqual(max_length,255)

    def test_recipe_difficulty(self):
        Recipe = Recipes.objects.get(recipe_id=1)

        max_length = Recipe._meta.get_field('difficulty').max_length

        self.assertEqual(max_length,12)
