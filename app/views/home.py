#  Project : KSRTC Seat Availability Notification System
#  Filename : home.py
#  Author : blacklist
#  Current modification time : Wed, 18 May 2022 at 11:10 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:10 PM India Standard Time

from django.http import HttpResponse


def index(request):
    return HttpResponse(f"Connection Successful")
