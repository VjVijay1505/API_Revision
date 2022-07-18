from rest_framework import serializers
from watchlist_app.models import Movie
from .serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def movies(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def movie(request,pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':        
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response('Content deleted!!')