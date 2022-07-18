from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.WatchList_List.as_view(), name = 'WatchList_List'),
    path('movies/<str:pk>', views.WatchList_Single.as_view(), name = 'WatchList_Single'),
    path('streammovies/', views.StreamPlatform_List.as_view(), name = 'StreamPlatform_List'),
    path('streammovies/<str:pk>', views.StreamPlatform_Single.as_view(), name = 'StreamPlatform_Single'),
]
