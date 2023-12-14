from rest_framework import serializers
from .models import  *




class CategorySerializer(serializers.ModelSerializer):
      class Meta:
          model  = Category
          fields = ['name']


class ImageNewsSerializer(serializers.ModelSerializer):
      class Meta:
          model  = ImageNews
          fields = ['image']



class VideoSerializer(serializers.ModelSerializer):
      class Meta:
          model  = Video
          fields = ['videos']



class FileSerializer(serializers.ModelSerializer):
      class Meta:
          model  =  FileBook
          fields = ['files']



class NewSerializer(serializers.ModelSerializer):
      category  = CategorySerializer()
      images = ImageNewsSerializer(many=True, read_only=True)


      class Meta:
          model  = News
          fields  = ['id', 'images', 'category', 'name', 'created_at']




class NewDetailSerializer(serializers.ModelSerializer):
     category = CategorySerializer()
     images = ImageNewsSerializer(many=True, read_only=True)


     class Meta:
          model  = News
          fields = ['category','created_at', 'images', 'title' ]




class FotoSerializer(serializers.ModelSerializer):
      cat  = CategorySerializer()
      img = ImageNewsSerializer(many=True, read_only=True)


      class Meta:
          model  = Fotogallery
          fields  = ['cat','id', 'created_at', 'img', 'body']




class FotoDetailSerializer(serializers.ModelSerializer):
      img = ImageNewsSerializer(many=True, read_only=True)


      class Meta:
          model  = Fotogallery
          fields  = ['img', 'body']


class VideoGallerySerializer(serializers.ModelSerializer):
      categ  = CategorySerializer()
      video = VideoSerializer(many=True, read_only=True)


      class Meta:
          model  = Videogallery
          fields  = ['categ','id', 'created_at', 'video', 'body']




class VideoDetailSerializer(serializers.ModelSerializer):
      video = VideoSerializer(many=True, read_only=True)


      class Meta:
          model  = Videogallery
          fields  = ['video', 'body']






class ActionSerializer(serializers.ModelSerializer):
      cat  = CategorySerializer()

      class Meta:
          model  = Action
          fields  = ['cat','id', 'created_at', 'img', 'body']


class InforSerializer(serializers.ModelSerializer):
      cate  = CategorySerializer()
      file = FileSerializer(many=True, read_only=True)


      class Meta:
          model  = Information
          fields  = ['cate','id', 'name', 'file']
