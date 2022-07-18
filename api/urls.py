from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies, name="movies"),
    path('movies/<str:pk>', views.movie, name="movie"),
]
