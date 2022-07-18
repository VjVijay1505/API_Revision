from django.db import models
import uuid


# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=200)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    
    def __str__(self):
        return self.title
