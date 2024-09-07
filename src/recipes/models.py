from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Recipes(models.Model):
    recipe_id=models.IntegerField()
    name=models.CharField(max_length=120)
    cooking_time=models.IntegerField()
    ingredients=models.CharField(max_length=255)
    difficulty=models.CharField(max_length=12)
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def get_absolute_url2(self):
        return reverse ('recipes:main',kwargs={'pk': self.pk})