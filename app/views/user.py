#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Mon, 23 May 2022 at 12:05 AM India Standard Time
#  Last modified time : Mon, 23 May 2022 at 12:05 AM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from app.libs import authenticate
from models import NotificationModel


class User:

    @staticmethod
    @beartype
    @authenticate
    def dynamic_pages(request: WSGIRequest, page: str) -> 'HttpResponse':
        data = {'page_title': f"{request.session['user_name']} - {page.title()} | KSRTC Seat Availability Notification",
                'notifications': NotificationModel.get_notifications(request.session['user'])}
        return render(request, f'user/{page}.html', data)
