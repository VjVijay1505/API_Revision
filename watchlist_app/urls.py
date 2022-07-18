from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),
    path('list/<str:pk>', views.movie_list_ind, name='movie-list-ind'),
]
