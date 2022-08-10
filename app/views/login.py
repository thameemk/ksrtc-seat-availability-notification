#  Project : KSRTC Seat Availability Notification System
#  Filename : login.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:22 PM India Standard Time
#  Last modified time : Thu, 19 May 2022 at 8:22 PM India Standard Time
import logging

from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.libs import Firebase
from app.models import UserModel


class Login:

    @staticmethod
    @beartype
    @csrf_exempt
    def auth_callback(request: WSGIRequest) -> 'HttpResponse':
        # todo - fix csrf token in login.html
        # todo - add full name in login.html
        # todo - submit phone number & otp button loader
        auth_user = Firebase().validate_token(request.headers['Bearer'])
        user = UserModel.get_user(auth_user['uid'])
        if user is None:
            user = UserModel.save_user(auth_user['uid'], auth_user['phone_number'], "Guest")
        request.session['user'] = user.uid
        request.session['user_name'] = user.full_name
        return HttpResponse("login_success")

    @staticmethod
    @beartype
    def login(request: WSGIRequest) -> 'HttpResponse':
        data = {'page_title': 'Login | KSRTC Seat Availability Notification'}
        return render(request, 'login.html', data)

    @staticmethod
    @beartype
    @csrf_exempt
    def logout(request: WSGIRequest) -> 'HttpResponse':
        try:
            del request.session['user']
        except Exception as e:
            logging.error((str(e)))
        return HttpResponse("logout_success")
