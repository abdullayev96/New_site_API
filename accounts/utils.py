import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import *

import datetime
import jwt



#
#
# def generate_otp(length=6):
#     characters = string.digits
#     otp = ''.join(random.choice(characters) for _ in range(length))
#     return otp
#
#
#
# def send_otp_email(email, otp):
#     subject = 'Your OTP for Login'
#     message = f'Your OTP is: {otp}'
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)
#


def send_otp_email(email):
    subject = 'Your account verification email is'
    otp  = random.randint(10000, 99999)
    from_email = settings.EMAIL_HOST
    message = f'This is Your  OTP {otp}'


    send_mail(subject, message, from_email, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()



def generate_access_token(user):

    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256').decode('utf-8')

    return refresh_token
