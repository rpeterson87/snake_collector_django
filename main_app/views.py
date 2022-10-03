import imp
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Snakes


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    
class About(TemplateView):
    template_name = ""
    
    
class SnakeList(TemplateView):
    template_name = "snake_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snakes"] = Snakes.objects.all() # Here we are using the model to query the database for us.
        return context