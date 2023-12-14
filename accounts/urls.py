from django.urls import path
from .views import *


from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView



urlpatterns = [
          path('register/', RegisterAPI.as_view()),
          path('login/', LoginAPI.as_view()),
          path('verify/', VerifyOTPAPI.as_view()),
          path('refresh/', TokenRefreshView.as_view()),
          path('token/', TokenObtainPairView.as_view()),
          path('verify/', TokenVerifyView.as_view()),

]