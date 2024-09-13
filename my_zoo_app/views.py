from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Animal, Donation
from .forms import ConservationForm

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animal_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    conservation_form = ConservationForm()
    return render(request, 'animals/detail.html', {
        'animal': animal, 'conservation_form': conservation_form
        })

def add_status(request, animal_id):
    form = ConservationForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.animal_id = animal_id
        new_status.save()
    return redirect('animal-detail', animal_id=animal_id)

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = '/animals/'

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['species', 'description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'

class DonationCreate(CreateView):
    model = Donation
    fields = '__all__'

class DonationList(ListView):
    model = Donation

class DonationDetail(DetailView):
    model = Donation

class DonationUpdate(UpdateView):
    model = Donation
    fields = ['amount']

class DonationDelete(DeleteView):
    model = Donation
    success_url = '/donations/'

