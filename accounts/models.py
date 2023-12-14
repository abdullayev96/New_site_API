from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken



#
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     otp = models.CharField(max_length=6, null=True, blank=True)
#
#
#
#     def __str__(self):
#         return self.username
#
#
#     class Meta:
#         verbose_name  = "Foydalanuvchi_"


class CustomUser(AbstractUser):
      username = models.CharField(max_length=300, unique=True)
      email =  models.EmailField(unique=True, blank=True)
      otp  = models.CharField(max_length=6, blank=True, null=True)
      is_staff = models.BooleanField(blank=False)



      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []

      #objects = UserManager()


      def save(self, *args, **kwargs):
          try:
             if kwargs['password']:
                  self.set_password(kwargs['password'])
          except Exception:
                       pass
          finally:
                super(CustomUser, self).save(*args, **kwargs)


      def tokens(self):
                refresh = RefreshToken.for_user(self)
                return {
                          'refresh': str(refresh),
                          'access': str(refresh.access_token)
                }

      class Meta:
          verbose_name = "Foydalanuvchi_"
