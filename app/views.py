#  Project : KSRTC Seat Availability Notification System
#  Filename : views.py
#  Author : blacklist
#  Current modification time : Mon, 16 May 2022 at 10:58 PM India Standard Time
#  Last modified time : Mon, 16 May 2022 at 10:58 PM India Standard Time
import fireo
from django.http import HttpResponse

fireo.connection(from_file="./serviceAccountKey.json")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
