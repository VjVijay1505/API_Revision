from rest_framework.serializers import ModelSerializer
from watchlist_app.models import Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)