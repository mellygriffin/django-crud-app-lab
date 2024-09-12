from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animal_index(request):
    return render(request, 'animals/index.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/detail.html', {'animal': animal})

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = '/animals/'

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['species', 'description', 'age', 'status']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'


