from django.shortcuts import render
from .models import WatchList
from django.http import JsonResponse

# Create your views here.
def movie_list(request):
    movies = WatchList.objects.all()
    context = {'movies':list(movies.values())}
    return JsonResponse(context)

def movie_list_ind(request,pk):
    movie = WatchList.objects.get(id=pk)
    print(movie)
    context = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
        'created_at': movie.created_at,
        'id': movie.id
        }
    return JsonResponse(context)
