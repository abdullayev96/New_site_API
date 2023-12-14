from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated



class CategoryAPI(ListAPIView):
      queryset = Category.objects.all()
      serializer_class = CategorySerializer

      permission_classes = [IsAuthenticated]



class ProjectAPI(ListAPIView):
      queryset = ProjectName.objects.all()
      serializer_class = ProjectSerializer



# class ProjectAPI(APIView):
#       def get(self, request):
#             try:
#                   project  = ProjectName.objects.all()
#                   serializers = ProjectSerializer(project, many=True)
#                   return Response({"status": status.HTTP_200_OK,"data": serializers.data})
#
#             except Exception as e:
#                   print(e)
#
#             return Response({"status": status.HTTP_404_NOT_FOUND})


class ProjectDetailAPI(APIView):
      def get(self, request, pk=None):
            try:
                  project  = ProjectName.objects.get(id=pk)
                  serializers = ProjectSerializerDetail(project, context={'request': self.request})
                  return Response({"status": status.HTTP_200_OK,"data": serializers.data})

            except Exception as e:
                  print(e)

            return Response({"status": status.HTTP_404_NOT_FOUND})

