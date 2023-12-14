from django.urls import path
from .views import *




urlpatterns = [
          path('', NewsAPI.as_view()),
          path('foto/', FotoGalleryAPI.as_view()),
          path('foto/<int:pk>/',DetailGalleryAPI.as_view()),
          path('action/',ActionAPI.as_view()),
          path('video/',VideoGalleryAPI.as_view()),
          path('video/<int:pk>/',VideoDetailAPI.as_view()),
          path('infor/',InformationAPI.as_view())

]