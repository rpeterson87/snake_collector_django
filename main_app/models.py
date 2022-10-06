import time
from django.contrib.auth.models import User
from django.db import models

class Snakes(models.Model):
# Create your models here.
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    species_info = models.TextField(max_length=1500)
    verified_species = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



class SnakeData(models.Model):

    habitats = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    data = models.ForeignKey(Snakes, on_delete=models.CASCADE, related_name="snakes")
    
    def __str__(self):
        return self.habitats
 
   
class SnakeLists(models.Model):
    title = models.CharField(max_length=150)
    food = models.CharField(max_length=150)
    list = models.ManyToManyField(SnakeData)
    def __str__(self):
        return self.title
    
    

    
