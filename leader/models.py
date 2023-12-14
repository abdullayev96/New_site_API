from django.db import models
from baseapp.models import BaseModel



class Category(BaseModel):
      name = models.CharField(max_length=200, verbose_name="Kategoriya nomi")

      def __str__(self):
          return self.name



class Leader(BaseModel):
      full_name = models.CharField(max_length=300, verbose_name="Rahbarni toliq ismi ")
      position =  models.CharField(max_length=200, verbose_name="Rahbar lavozimi")
      image = models.ImageField(upload_to='image/')
      phone = models.CharField(max_length=40, verbose_name="telefon nomeri")
      email  = models.EmailField(verbose_name="Elektron pochtasi")
      facebook = models.CharField(max_length=100, verbose_name="Facebook lichkasi")
      whatsapp = models.CharField(max_length=100, verbose_name="Whatsapp lichkasi")
      instagram = models.CharField(max_length=100, verbose_name="Instagram lichkasi")
      admission_days = models.CharField(max_length=400, verbose_name="Qabul qilish kunlari")
      work_activity   = models.CharField(max_length=200, verbose_name="Ish faoliyati")
      tasks_functions = models.CharField(max_length=300, verbose_name="Vazifa va funsiyalari")
      category = models.ForeignKey(Category, on_delete=models.CASCADE)


      def __str__(self):
          return self.full_name

      class Meta:
          verbose_name = "Rahbar"



class Agency(BaseModel):

      image  = models.ImageField(upload_to='about/')
      title = models.TextField()
      category = models.ForeignKey(Category, on_delete=models.CASCADE)

      def __str__(self):
          return self.title


      class Meta:
           verbose_name='Biz haqimzda'


class Purpose(BaseModel):
      name = models.CharField(max_length=300, verbose_name="Maqsad va vazifa nomi")
      title  = models.TextField()
      category = models.ForeignKey(Category, on_delete=models.CASCADE)


      def __str__(self):
          return self.name

      class Meta:
            verbose_name = "Maqsad va vazifa"


class RegionOffice(BaseModel):
      full_name = models.CharField(max_length=300, verbose_name="Boshliq to'liq ismi ")
      image = models.ImageField(upload_to='img/')
      position = models.CharField(max_length=200, verbose_name="Rahbar lavozimi")
      facebook = models.CharField(max_length=100, verbose_name="Facebook lichkasi")
      whatsapp = models.CharField(max_length=100, verbose_name="Whatsapp lichkasi")
      instagram = models.CharField(max_length=100, verbose_name="Instagram lichkasi")
      category  = models.ForeignKey(Category, on_delete=models.CASCADE)

      def __str__(self):
          return self.full_name


      class Meta:
            verbose_name = "Hudud boshqarmasi"


class Tizim(BaseModel):
      name = models.CharField(max_length=299, verbose_name="Tuzilma nomi")
      image  = models.ImageField(upload_to="tizim/", verbose_name="")
      body = models.CharField(max_length=299, verbose_name="Tuzilma haqida")



      def __str__(self):
          return self.name


      class Meta:
            verbose_name = "Agentlik tuzilmasi"

