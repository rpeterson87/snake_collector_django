from django.contrib import admin
from .models import Snakes # import the Artist model from models.py
# Register your models here.

admin.site.register(Snakes) # this line will add the model to the admin panel