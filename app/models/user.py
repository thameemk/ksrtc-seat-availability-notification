#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : blacklist
#  Current modification time : Sun, 15 May 2022 at 7:33 PM India Standard Time
#  Last modified time : Sun, 15 May 2022 at 7:33 PM India Standard Time
import pendulum
from fireo.fields import TextField, NumberField, DateTime, BooleanField
from fireo.models import Model


class UserModel(Model):
    full_name = TextField(required=True)
    phone = NumberField(required=True)
    is_deleted = BooleanField(required=True, default=False)
    created_on = DateTime(required=True, default=pendulum.now().utcnow)
    modified_on = DateTime(required=True, default=pendulum.now().utcnow)
