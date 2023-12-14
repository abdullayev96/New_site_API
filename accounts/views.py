from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import *
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import *
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView

from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie

from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware import csrf

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterAPI(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer  = RegisterSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                send_otp_email(serializer.data['email'])
                return Response({"data":status.HTTP_201_CREATED})

        except Exception as e:
            print(e)

        return Response({"status":status.HTTP_400_BAD_REQUEST})


# class ValidateOTP(APIView):
#     def post(self, request):
#         email = request.data.get('email', '')
#         otp = request.data.get('otp', '')
#
#         try:
#             user = CustomUser.objects.get(email=email)
#         except CustomUser.DoesNotExist:
#             return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
#
#         if user.otp == otp:
#             user.otp = None
#             user.save()
#
#             token, _ = Token.objects.get_or_create(user=user)
#
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
#

class VerifyOTPAPI(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = CustomUser.objects.filter(email=email)
                if not user.exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "Try again IT is wrong ",
                                     "data": "Invalid OTP or email"})

                if not user[0].otp != otp:
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "try again It is wrong ",
                                     "data": "wrong  OTP "})

                user = user.first()
                user.is_staff = True
                user.save()

                return Response({"status": status.HTTP_200_OK,
                                 "message": "Your account activate",
                                 "data": serializer.data})

            return Response({"status": status.HTTP_404_NOT_FOUND})


        except Exception as e:
            print(e)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }



class LoginAPI(APIView):
    def post(self, request):
        try:
           email = request.data.get('email')
           password = request.data.get('password')

           user = authenticate(email=email, password=password)

           data = get_tokens_for_user(user)
           return Response({'data': data})

        except Exception as e:
            print(e)


        return  Response({'status':status.HTTP_404_NOT_FOUND})





# class LoginAPI(APIView):
#     def post(self, request, format=None):
#         data = request.data
#         response = Response()
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             if user.is_active:
#                 data = get_tokens_for_user(user)
#                 response.set_cookie(
#                     key=settings.SIMPLE_JWT['AUTH_COOKIE'],
#                     value=data["access_token"],
#                     expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
#                     secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#                     httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#                     samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
#                 )
#                 response.set_cookie(
#                     key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
#                     value=data["refresh_token"],
#                     expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
#                     secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#                     httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#                     samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
#                 )
#
#                 csrf.get_token(request)
#                 response.data = {"Success": "Login successfully"}
#                 return response
#             else:
#                 return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
#


class RefreshAPI(APIView):
    def get(self, request, format=None):
        refresh_token = request.COOKIES.get(
            settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        if refresh_token is None:
            raise AuthenticationFailed(
                'Authentication credentials were not provided.')

        token = RefreshToken(refresh_token)
        response = Response()
        response.data = {'message': 'Successfully refreshed'}
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=str(token.access_token),
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        return response




# @api_view(['POST'])
# @permission_classes([AllowAny])
# @ensure_csrf_cookie
# def LoginAPI(request):
#
#     email = request.data.get('email')
#     password = request.data.get('password')
#
#     user = authenticate(email=email, password=password)
#     #
#     # email = request.data.get('email')
#     # password = request.data.get('password')
#     # response = Response()
#     # if (email is None) or (password is None):
#     #     raise exceptions.AuthenticationFailed('username and password required')
#     #
#     # user = CustomUser.objects.filter(email=email).first()
#     # if(user is None):
#     #     raise exceptions.AuthenticationFailed('user not found')
#     # if (not user.check_password(password)):
#     #     raise exceptions.AuthenticationFailed('wrong password')
#
#     serialized_user = RegisterSerializer(user).data
#
#     access_token = generate_access_token(user)
#     refresh_token = generate_refresh_token(user)
#
#     response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
#     response.data = {
#         'access_token': access_token,
#         'user': serialized_user,
#     }
#
#     return response
