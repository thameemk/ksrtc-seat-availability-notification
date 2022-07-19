#  Project : KSRTC Seat Availability Notification System
#  Filename : service_location.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:50 PM India Standard Time

import pendulum
from fireo.fields import TextField, IDField, DateTime
from fireo.models import Model


class ServiceLocationModel(Model):
    class Meta:
        collection_name = "service_locations"

    location_id = IDField(required=True)
    location_name = TextField(required=True)
    created_on = DateTime(required=True, default=pendulum.now().utcnow)
    modified_on = DateTime(required=True, default=pendulum.now().utcnow)
