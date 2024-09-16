from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animal_index, name='animal-index'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal-detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal-update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal-delete'),
    path(
        'animals/<int:animal_id>/add-status/',
        views.add_status,
        name='add-status'
    ),
    path('donations/create/', views.DonationCreate.as_view(), name='donation-create'),
    path('donations/<int:pk>/', views.DonationDetail.as_view(), name='donation-detail'),
    path('donations/', views.DonationList.as_view(), name='donation-index'),
    path('donations/<int:pk>/update/', views.DonationUpdate.as_view(), name='donation-update'),
    path('donations/<int:pk>/delete', views.DonationDelete.as_view(), name='donation-delete'),
    path('accounts/signup/', views.signup, name='signup'),

]
