from django.contrib import admin
from .models import SnakeLists, Snakes, SnakeData


admin.site.register(Snakes) 
admin.site.register(SnakeData) 
admin.site.register(SnakeLists)