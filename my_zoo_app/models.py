from django.db import models
from django.urls import reverse

CONSERVATION_STATUS = (
    ('LR', 'Low Risk'),
    ('VR', 'Vulnerable'),
    ('ED', 'Endangered'),
    ('CE', 'Critically Endangered'),
)

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("animal-detail", kwargs={"animal_id": self.id})
    
    
class Conservation(models.Model):
    status=models.CharField(
        max_length=2,
        choices=CONSERVATION_STATUS,
        default=CONSERVATION_STATUS[0][0]
    )