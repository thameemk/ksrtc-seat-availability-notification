#  Project : KSRTC Seat Availability Notification System
#  Filename : notification.py
#  Author : blacklist
#  Current modification time : Sun, 15 May 2022 at 7:56 PM India Standard Time
#  Last modified time : Sun, 15 May 2022 at 7:56 PM India Standard Time
import pendulum
from fireo.fields import ReferenceField, BooleanField, DateTime, NumberField
from fireo.models import Model

from firebase_db_models import ServiceLocationModel, UserModel


class NotificationModel(Model):
    leaving_from = ReferenceField(ServiceLocationModel, required=True)
    going_to = ReferenceField(ServiceLocationModel, required=True)
    date_of_departure = DateTime(required=True)
    date_of_return = DateTime()
    user = ReferenceField(UserModel, required=True)
    is_active = BooleanField(required=True, default=True)
    time_interval = NumberField(required=True)
    receive_notification_up_to = DateTime(required=True)
    created_on = DateTime(required=True, default=pendulum.now().utcnow)
    modified_on = DateTime(required=True, default=pendulum.now().utcnow)
