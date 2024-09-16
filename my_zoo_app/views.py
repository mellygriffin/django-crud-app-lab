from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Animal, Donation
from .forms import ConservationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def animal_index(request):
    animals = Animal.objects.filter(user=request.user)
    return render(request, 'animals/index.html', {'animals': animals})

@login_required
def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    conservation_form = ConservationForm()
    return render(request, 'animals/detail.html', {
        'animal': animal, 'conservation_form': conservation_form
        })

@login_required
def add_status(request, animal_id):
    form = ConservationForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.animal_id = animal_id
        new_status.save()
    return redirect('animal-detail', animal_id=animal_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animal-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = '__all__'
    success_url = '/animals/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['species', 'description', 'age']

class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = '/animals/'

class DonationCreate(LoginRequiredMixin, CreateView):
    model = Donation
    fields = '__all__'

class DonationList(LoginRequiredMixin, ListView):
    model = Donation

class DonationDetail(LoginRequiredMixin, DetailView):
    model = Donation

class DonationUpdate(LoginRequiredMixin, UpdateView):
    model = Donation
    fields = ['amount']

class DonationDelete(LoginRequiredMixin, DeleteView):
    model = Donation
    success_url = '/donations/'

