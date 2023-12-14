from django.urls import path
from .views import *



urlpatterns = [
          path('', LeaderAPI.as_view()),
          path('<int:pk>/', DetailLeaderAPI.as_view()),
          path('agen/', AgencyAPI.as_view()),
          path('purpose/', PurposeAPI.as_view()),
          path('region/', RegionAPI.as_view()),
          path('tizim/', TizimAPI.as_view())
]