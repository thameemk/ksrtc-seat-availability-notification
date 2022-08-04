#  Project : KSRTC Seat Availability Notification System
#  Filename : notification.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:36 PM India Standard Time
from typing import Optional

import pendulum
from beartype import beartype
from fireo.fields import ReferenceField, BooleanField, DateTime, NumberField
from fireo.models import Model

from app.models import LocationModel, UserModel


class NotificationModel(Model):
    class Meta:
        collection_name = "notifications"

    leaving_from = ReferenceField(LocationModel, required=True)
    going_to = ReferenceField(LocationModel, required=True)
    date_of_departure = DateTime(required=True)
    date_of_return = DateTime()
    user = ReferenceField(UserModel, required=True)
    is_active = BooleanField(required=True, default=True)
    time_interval = NumberField(required=True)
    receive_notification_up_to = DateTime(required=True)
    created_on = DateTime(required=True, default=pendulum.now().utcnow)
    modified_on = DateTime(required=True, default=pendulum.now().utcnow)

    @classmethod
    @beartype
    def get_notifications(cls, user: str) -> Optional[list['NotificationModel']]:
        return [each for each in cls.collection.fetch() if each.user == user]
