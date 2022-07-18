from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform
from django.utils.timezone import now

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    joined_since = serializers.SerializerMethodField()
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
    def validate(self, data):
        if len(data['name']) < 3:
            raise serializers.ValidationError('Too Short!!')
        return data
    
    def get_joined_since(self, object):
        return (now() - object.created_at).days
    

class WatchListSerializer(serializers.ModelSerializer):
    
    joined_since = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        
    def validate(self, data):
        if len(data['title']) < 3:
            raise serializers.ValidationError('Too Short!!')
        return data
    
    def get_joined_since(self, object):
        return (now() - object.created_at).days