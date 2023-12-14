from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .serializers import *
from .models import *



class NewsAPI(ListAPIView):
     queryset = News.objects.all()
     serializer_class = NewSerializer



class FotoGalleryAPI(APIView):
     def get(self, request):
         try:
             foto = Fotogallery.objects.all()
             serializer = FotoSerializer(foto, many=True, context={'request': self.request})
             return Response({"status": status.HTTP_200_OK,"data": serializer.data})

         except Exception as e:
              print(e)

         return Response({"status": status.HTTP_404_NOT_FOUND})



class DetailGalleryAPI(APIView):
     def get(self, request, pk=None):
         try:
             foto = Fotogallery.objects.get(id=pk)
             serializer = FotoDetailSerializer(foto, context={'request': self.request})
             return Response({"status": status.HTTP_200_OK,"data": serializer.data})

         except Exception as e:
              print(e)

         return Response({"status": status.HTTP_404_NOT_FOUND})




class VideoGalleryAPI(APIView):
     def get(self, request):
         try:
             foto = Videogallery.objects.all()
             serializer = VideoGallerySerializer(foto, many=True, context={'request': self.request})
             return Response({"data": serializer.data})

         except Exception as e:
              print(e)

         return Response({"status": status.HTTP_404_NOT_FOUND})


class VideoDetailAPI(APIView):
     def get(self, request, pk=None):
         try:
             foto = Videogallery.objects.get(id=pk)
             serializer = VideoDetailSerializer(foto, context={'request':self.request})
             return Response({"data": serializer.data})

         except Exception as e:
              print(e)

         return Response({"status": status.HTTP_404_NOT_FOUND})



class ActionAPI(APIView):
     def get(self, request):
         try:
             foto = Action.objects.all()
             serializer = ActionSerializer(foto, many=True, context={'request': self.request})
             return Response({"data": serializer.data})

         except Exception as e:
              print(e)

         return Response({"status": status.HTTP_404_NOT_FOUND})


class InformationAPI(ListAPIView):
     queryset = Information.objects.all()
     serializer_class = InforSerializer



#
# class InformationAPI(APIView):
#      def get(self, request):
#          try:
#              foto = Information.objects.all()
#              serializer = InforSerializer(foto, many=True, context={'request':self.request})
#              return Response({"data": serializer.data})
#
#          except Exception as e:
#               print(e)
#
#          return Response({"status": status.HTTP_404_NOT_FOUND})