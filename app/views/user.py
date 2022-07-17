#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Mon, 23 May 2022 at 12:05 AM India Standard Time
#  Last modified time : Mon, 23 May 2022 at 12:05 AM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


class User:
    @beartype
    def __init__(self) -> None:
        pass

    @beartype
    def home(self, request: WSGIRequest) -> 'HttpResponse':
        return render(request, 'user/home.html')
