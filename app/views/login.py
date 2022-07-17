#  Project : KSRTC Seat Availability Notification System
#  Filename : login.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:22 PM India Standard Time
#  Last modified time : Thu, 19 May 2022 at 8:22 PM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from libs import FirebaseAuth
from models import UserModel


class Login:

    @staticmethod
    @beartype
    def auth_callback(request: WSGIRequest) -> 'HttpResponse':
        # todo - check user in db, if not, validate firebase uid and save
        firebase_uid = FirebaseAuth().validate_token(request.headers['Bearer'])
        UserModel.get_user(firebase_uid)
        return HttpResponse("login_success")

    @staticmethod
    @beartype
    def login(request: WSGIRequest) -> 'HttpResponse':
        data = {'page_title': 'Login | KSRTC Seat Availability Notification'}
        return render(request, 'login.html', data)
