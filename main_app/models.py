from django.db import models

class Snakes(models.Model):
# Create your models here.
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    species_info = models.TextField(max_length=500)
    verified_species = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
