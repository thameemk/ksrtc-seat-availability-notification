#  Project : KSRTC Seat Availability Notification System
#  Filename : settings.py
#  Author : blacklist
#  Current modification time : Sun, 17 Apr 2022 at 11:27 PM India Standard Time
#  Last modified time : Sun, 17 Apr 2022 at 11:27 PM India Standard Time
from decouple import config

KSRTC_HOME_URL = config('KSRTC_HOME_URL', default="", cast=str)
