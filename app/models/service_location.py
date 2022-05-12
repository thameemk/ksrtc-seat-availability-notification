#  Project : KSRTC Seat Availability Notification System
#  Filename : service_location.py
#  Author : blacklist
#  Current modification time : Sat, 7 May 2022 at 8:08 PM India Standard Time
#  Last modified time : Sat, 7 May 2022 at 8:08 PM India Standard Time
from fireo.fields import TextField, IDField
from fireo.models import Model


class ServiceLocation(Model):
    location_id = IDField(required=True)
    location_name = TextField(required=True)
