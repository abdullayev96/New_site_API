from django.db import models
from baseapp.models  import BaseModel


class Category(BaseModel):
      name = models.CharField(max_length=200, verbose_name="Loyiha nomi")


      def __str__(self):
          return self.name


      class Meta:
          verbose_name = "Kategoriya"



class ProjectName(BaseModel):
      cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
      name = models.CharField(max_length=200, verbose_name="Loyiha nomi")
      image = models.ImageField(upload_to="img/")
      body  = models.TextField(verbose_name="Loyiha haqida")
      facebook = models.CharField(max_length=100, verbose_name="Facebook lichkasi")
      whatsapp = models.CharField(max_length=100, verbose_name="Whatsapp lichkasi")
      instagram = models.CharField(max_length=100, verbose_name="Instagram lichkasi")


      def __str__(self):
          return self.name

      class Meta:
           verbose_name= "Loyiha"


