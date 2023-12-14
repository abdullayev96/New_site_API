from django.db import models
from baseapp.models import BaseModel

import os
from django.core.exceptions import ValidationError



def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.xlsx', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .pdf, .doc, .xlsx, .jpg  file ')




class Category(models.Model):
       name  = models.CharField(max_length=200, verbose_name="Categoriya nomi")


       def __str__(self):
           return self.name

       class Meta:
             verbose_name = "Kategoriya"



class ImageNews(models.Model):
      image = models.ImageField(upload_to='yes/', verbose_name="rasm yuklash")


      class Meta:
          verbose_name  = "Rasm qo'shish"



class  News(BaseModel):
       name = models.CharField(max_length=300, verbose_name="Yangilik nomi")
       title = models.TextField()
       images = models.ManyToManyField(ImageNews, related_name='images')
       category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

       def __str__(self):
          return self.name

       class Meta:
            verbose_name = "Yangilik"



class Fotogallery(BaseModel):
      img = models.ManyToManyField(ImageNews, related_name='img')
      body  = models.TextField(verbose_name="rasmlar haqida")
      cat = models.ForeignKey(Category, on_delete=models.CASCADE)


      def __str__(self):
          return self.body


      class Meta:
          verbose_name= "FotoGaleriya"




class Video(models.Model):
      videos  = models.FileField(upload_to='video/', verbose_name="Videolar", blank=True,null=True)


      class Meta:
          verbose_name = "Videolar"



class Videogallery(BaseModel):
      video = models.ManyToManyField(Video, related_name='video')
      body  = models.TextField(verbose_name="rasmlar haqida")
      categ = models.ForeignKey(Category, on_delete=models.CASCADE)

      def get_videos(self, obj):
            return "\n".join([p.videos for p in obj.video.all()])


      def __str__(self):
          return self.body


      class Meta:
          verbose_name= "VideoGaleriya"

#


class FileBook(models.Model):
      files  = models.FileField(upload_to='audio/', verbose_name="Faylni tanlang", validators=[validate_file])

      class Meta:
          verbose_name = "Malumot fayl"




class Information(BaseModel):
      name  = models.CharField(max_length=300, verbose_name="Malumot nomi")
      file  = models.ManyToManyField(FileBook, related_name="file")
      cate = models.ForeignKey(Category, on_delete=models.CASCADE)

      def __str__(self):
          return self.name

      class Meta:
          verbose_name = 'Malumotlar'




class Action(BaseModel):
      name = models.CharField(max_length=200, verbose_name="Rasm nomi")
      img = models.ImageField(upload_to='img/', verbose_name="Tadbir rasmlari")
      body  = models.TextField(verbose_name="rasmlar haqida")
      cat = models.ForeignKey(Category, on_delete=models.CASCADE)


      def __str__(self):
          return self.name


      class Meta:
          verbose_name= "Tadbirlar"



