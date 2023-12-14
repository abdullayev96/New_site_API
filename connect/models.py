from django.db import models
from baseapp.models import BaseModel



class Message(BaseModel):
      full_name = models.CharField(max_length=200, verbose_name="Foylanuvchi ismi")
      email  = models.EmailField(unique=True)
      phone = models.CharField(max_length=100, verbose_name="Telefon raqami")
      subject  = models.CharField(max_length=300, verbose_name="Mavzu nomi")
      message = models.CharField(max_length=200, verbose_name="Xabar matni")


      def __str__(self):
          return self.full_name


      class Meta:
          verbose_name = "Xabarlar"
