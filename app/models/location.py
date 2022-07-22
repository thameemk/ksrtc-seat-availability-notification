#  Project : KSRTC Seat Availability Notification System
#  Filename : location.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:50 PM India Standard Time
from datetime import datetime

from beartype import beartype
from fireo.fields import TextField, IDField, DateTime
from fireo.models import Model


class LocationModel(Model):
    class Meta:
        collection_name = "locations"

    location_id = IDField(required=True)
    location_name = TextField(required=True)
    created_on = DateTime(required=True, default=datetime.now())
    modified_on = DateTime(required=True, default=datetime.now())

    @classmethod
    @beartype
    def save_location(cls, location_id: str, location_name: str) -> 'LocationModel':
        location = LocationModel(
            location_id=location_id,
            location_name=location_name
        ).save()

        return location


