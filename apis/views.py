from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform
from .serializer import WatchListSerializer, StreamPlatformSerializer
from rest_framework import status

class StreamPlatform_List(APIView):
    
    def get(self, request):
        movies = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(movies, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class StreamPlatform_Single(APIView):
    
    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(movie)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(id=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'Message':'Deleted'}, status = status.HTTP_202_ACCEPTED)

class WatchList_List(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class WatchList_Single(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request,pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'Message':'Deleted'}, status = status.HTTP_202_ACCEPTED)
    