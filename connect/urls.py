from django.urls import path
from .views import MessageAPI


urlpatterns  = [
          path('', MessageAPI.as_view())
]