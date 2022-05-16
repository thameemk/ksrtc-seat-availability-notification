#  Project : KSRTC Seat Availability Notification System
#  Filename : urls.py
#  Author : blacklist
#  Current modification time : Mon, 16 May 2022 at 10:59 PM India Standard Time
#  Last modified time : Mon, 16 May 2022 at 10:59 PM India Standard Time
from django.urls import path

import views

urlpatterns = [
    path('', views.index, name='index'),
]
