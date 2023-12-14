from django.urls import path
from .views import *


urlpatterns  = [
          path('category/', CategoryAPI.as_view()),
          path('pro/', ProjectAPI.as_view()),
          path('pro/<int:pk>/', ProjectDetailAPI.as_view())

]