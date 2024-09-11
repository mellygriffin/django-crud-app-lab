from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


# views.py

class Animal:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

# Create a list of Cat instances
animals = [
    Animal('Lolo', 'tabby', 'Kinda rude.', 3),
    Animal('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Animal('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Animal('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def animal_index(request):
    return render(request, 'animals/index.html', {'animals': animals})
