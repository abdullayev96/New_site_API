from rest_framework  import serializers
from .models import *



class CategorySerilazer(serializers.ModelSerializer):
      class Meta:
          model = Category
          fields  = ['name']


class LeaderSerializer(serializers.ModelSerializer):
      category = CategorySerilazer()

      class Meta:
          model  = Leader
          fields  = ['category', 'id','image', 'full_name','facebook','whatsapp','instagram', 'position']




class DetailSerializer(serializers.ModelSerializer):
     class Meta:
          model = Leader
          fields  = ['image', 'full_name','position','phone','email','admission_days','facebook',
                     'whatsapp','instagram', 'work_activity','tasks_functions']




class AgencySerializer(serializers.ModelSerializer):
     category = CategorySerilazer()
     class Meta:
          model = Agency
          fields  = ['category','image', 'title']



class PurposeSerializer(serializers.ModelSerializer):
     category = CategorySerilazer()
     class Meta:
          model = Purpose
          fields  = ['category','id','name', 'title']



class RegionSerializer(serializers.ModelSerializer):
      category = CategorySerilazer()

      class Meta:
           model = RegionOffice
           fields = ['category','id','image', 'full_name', 'position', 'facebook','whatsapp', 'instagram']



class TizimSerializer(serializers.ModelSerializer):
          class Meta:
              model = Tizim
              fields = ['id', 'name', 'image', 'body']



