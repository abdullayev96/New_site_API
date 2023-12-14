from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Message
from .serializers import MessageSerializer



class MessageAPI(CreateAPIView):
      queryset = Message.objects.all()
      serializer_class = MessageSerializer



