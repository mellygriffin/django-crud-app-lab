from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CONSERVATION = (
    ('LR', 'Low Risk'),
    ('VR', 'Vulnerable'),
    ('ED', 'Endangered'),
    ('CE', 'Critically Endangered'),
)

# Create your models here.
class Donation(models.Model):
    donor = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.donor
    
    def get_absolute_url(self):
        return reverse('donation-detail', kwargs={'pk': self.id})

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("animal-detail", kwargs={"animal_id": self.id})
    
    
class Conservation(models.Model):
    date = models.DateField('Date Changed')
    status=models.CharField(
        max_length=2,
        choices=CONSERVATION,
        default=CONSERVATION[0][0]
    )

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

