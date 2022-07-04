#  Project : KSRTC Seat Availability Notification System
#  Filename : login.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:22 PM India Standard Time
#  Last modified time : Thu, 19 May 2022 at 8:22 PM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


class Login:

    @staticmethod
    @beartype
    @csrf_exempt
    def auth_callback(request: WSGIRequest) -> 'HttpResponse':
        # todo - check user in db, if not, validate firebase uid and save
        return HttpResponse("login_success")

    @staticmethod
    @beartype
    def login(request: WSGIRequest) -> 'HttpResponse':
        data = {'page_title': 'Login | KSRTC Seat Availability Notification'}
        return render(request, 'login.html', data)
