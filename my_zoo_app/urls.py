from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animal_index, name='animal-index'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal-detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal-update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal-delete'),
]
