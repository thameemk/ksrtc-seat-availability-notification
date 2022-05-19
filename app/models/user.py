#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:50 PM India Standard Time

from datetime import datetime

from fireo.fields import TextField, NumberField, DateTime, BooleanField, IDField
from fireo.models import Model


class UserModel(Model):
    class Meta:
        collection_name = "users"

    full_name = TextField(required=True)
    phone = NumberField(required=True)
    is_deleted = BooleanField(required=True, default=False)
    created_on = DateTime(required=True, default=datetime.now())
    modified_on = DateTime(required=True, default=datetime.now())
