from multiprocessing import context
from django.urls import reverse
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import SnakeLists, Snakes, SnakeData
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snakes"] = SnakeLists.objects.all()
        return context
    
    
class About(TemplateView):
    template_name = "about.html"
    
    
    
class SnakeList(TemplateView):
    template_name = "snake_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["snakes"] = Snakes.objects.filter(name__icontains=name)
            # context["snakes"] = Snakes.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["snakes"] = Snakes.objects.all()
            context["header"] = "Top Snake Species"
        return context
 
@method_decorator(login_required, name='dispatch')    
class SnakeCreate(CreateView):
    model = Snakes
    fields = ['name', 'img', 'species_info', 'verified_species']
    template_name = 'snakes_create.html'
    def get_success_url(self):
        return reverse('snakes_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SnakeCreate, self).form_valid(form)
    

class SnakesDetail(DetailView):
    model = Snakes
    template_name = 'snakes_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = SnakeLists.objects.all()
        return context
    
 
class SnakeUpdate(UpdateView):
    model = Snakes
    fields = ['name', 'img', 'species_info', 'verified_species']
    template_name = 'snakes_update.html'
    def get_success_url(self):
        return reverse('snakes_detail', kwargs={'pk': self.object.pk})
    

 
class SnakeDelete(DeleteView):
    model = Snakes
    template_name = "snakes_delete_confirmation.html"
    success_url = "/snakes/"
   

class SnakesCreate(View):

    def post(self, request, pk):
        habitats = request.POST.get("habitats")
        length = request.POST.get("length")
        data = Snakes.objects.get(pk=pk)
        SnakeData.objects.create(habitats=habitats, length=length, data=data)
        return redirect('snakes_detail', pk=pk)


    
class SnakelistDataAssoc(View):

    def get(self, request, pk, snake_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            SnakeLists.objects.get(pk=pk).list.remove(snake_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            SnakeLists.objects.get(pk=pk).list.add(snake_pk)
        return redirect('home')
    
    

    

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("snake_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

    

    