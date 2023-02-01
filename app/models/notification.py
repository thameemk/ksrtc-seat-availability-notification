#  Project : KSRTC Seat Availability Notification System
#  Filename : notification.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:36 PM India Standard Time
from datetime import datetime
from typing import Optional

from beartype import beartype
from fireo.fields import ReferenceField, BooleanField, DateTime, NumberField, IDField
from fireo.models import Model

from app.models import LocationModel, UserModel


class NotificationModel(Model):
    class Meta:
        collection_name = "notifications"

    notification_id = IDField(required=True)
    leaving_from = ReferenceField(LocationModel, required=True)
    going_to = ReferenceField(LocationModel, required=True)
    date_of_departure = DateTime(required=True)
    date_of_return = DateTime()
    user = ReferenceField(UserModel, required=True)
    is_active = BooleanField(required=True, default=True)
    time_interval = NumberField(required=True)
    available_seats = NumberField(required=True)
    created_on = DateTime(required=True, default=datetime.now())
    modified_on = DateTime(required=True, default=datetime.now())

    @classmethod
    @beartype
    def get_notifications(cls, user: str) -> Optional[list['NotificationModel']]:
        return [each for each in cls.collection.fetch() if each.user.key == f'users/{user}']

    @classmethod
    @beartype
    def save_notification(cls, notification: 'NotificationModel') -> 'NotificationModel':
        return notification.save()

    @classmethod
    @beartype
    def get_notification(cls, user: str, notification_id: str) -> 'NotificationModel':
        _notification = cls(notification_id=notification_id)
        try:
            _notification = cls.collection.get(_notification.key)
            if _notification.user.key == f'users/{user}':
                return _notification
        except Exception:
            raise Exception("no matching model found with th requested id")
