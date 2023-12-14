from rest_framework  import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
          class Meta:
              model = Category
              fields = ['name']



class ProjectSerializer(serializers.ModelSerializer):
          cat = CategorySerializer()
          class Meta:
              model = ProjectName
              fields  = ['id','cat','name', 'image']




class ProjectSerializerDetail(serializers.ModelSerializer):
          class Meta:
              model = ProjectName
              fields  = ['name','created_at', 'image', 'body', 'facebook', 'whatsapp', 'instagram']

