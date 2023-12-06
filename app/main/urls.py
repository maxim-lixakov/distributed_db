from django.urls import path
from .views import add_cinema

urlpatterns = [
    path('add-cinema/', add_cinema, name='add_cinema'),
]