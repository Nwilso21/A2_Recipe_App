from django.db import models

# Create your models here.


class Recipes(models.Model):
    recipe_id=models.IntegerField()
    name=models.CharField(max_length=120)
    cooking_time=models.IntegerField()
    ingredients=models.CharField(max_length=255)
    difficulty=models.CharField(max_length=12)

    def __str__(self):
        return str(self.name)