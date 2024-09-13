from django.contrib import admin
from .models import Animal, Conservation, Donation

# Register your models here.
admin.site.register(Animal)
admin.site.register(Conservation)
admin.site.register(Donation)