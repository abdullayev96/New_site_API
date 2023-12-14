from django.shortcuts import render
from .models import Leader
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from .serializers import *



class LeaderAPI(APIView):
      def get(self, request):
          try:
             leader = Leader.objects.all()
             serializer = LeaderSerializer(leader, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)

          except Exception as e:
                    print(e)

          return Response(status=status.HTTP_404_NOT_FOUND)




class DetailLeaderAPI(APIView):
      def get(self, request, pk=None):
          try:
              leader_id= Leader.objects.get(id=pk)
              serializer  = DetailSerializer(leader_id)
              return Response(serializer.data , status=status.HTTP_200_OK)
          except Exception as e:
                    print(e)

          return Response(status=status.HTTP_404_NOT_FOUND)




class AgencyAPI(GenericAPIView):
      serializer_class = AgencySerializer

      def get(self, request):
          try:
             leader = Agency.objects.all()
             serializer = self.serializer_class(leader, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)

          except Exception as e:
                    print(e)

          return Response(status=status.HTTP_404_NOT_FOUND)



class PurposeAPI(GenericAPIView):
      serializer_class = PurposeSerializer

      def get(self, request):
          try:
             leader = Purpose.objects.all()
             serializer = self.serializer_class(leader, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)

          except Exception as e:
                    print(e)

          return Response(status=status.HTTP_404_NOT_FOUND)


class RegionAPI(ListAPIView):
      queryset = RegionOffice.objects.all()
      serializer_class = RegionSerializer




class TizimAPI(APIView):

      def get(self, request):
          try:
             tizim = Tizim.objects.all()
             serializer = TizimSerializer(tizim, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)

          except Exception as e:
                    print(e)

          return Response(status=status.HTTP_404_NOT_FOUND)

