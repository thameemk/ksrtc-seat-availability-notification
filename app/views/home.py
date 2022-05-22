#  Project : KSRTC Seat Availability Notification System
#  Filename : home.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Thu, 19 May 2022 at 12:23 AM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


@beartype
def index(request: WSGIRequest) -> 'HttpResponse':
    return HttpResponse("Connection Successful")
