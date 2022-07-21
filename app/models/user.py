#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:50 PM India Standard Time
from datetime import datetime
from typing import Optional

from beartype import beartype
from fireo.fields import TextField, DateTime, BooleanField, IDField
from fireo.models import Model


class UserModel(Model):
    class Meta:
        collection_name = "users"

    uid = IDField(required=True)
    full_name = TextField(required=True)
    phone_number = TextField(required=True)
    is_deleted = BooleanField(required=True, default=False)
    user_type = TextField(required=True, default="user")  # todo - update permission using deny
    created_on = DateTime(required=True, default=datetime.now())
    modified_on = DateTime(required=True, default=datetime.now())

    @classmethod
    @beartype
    def save_user(cls, firebase_uid: str, phone: str, full_name: str, ) -> 'UserModel':
        user = UserModel()
        user.uid = firebase_uid
        user.phone_number = phone
        user.full_name = full_name
        user.save()
        return user

    @classmethod
    @beartype
    def get_user(cls, firebase_uid: str) -> Optional['UserModel']:
        _user = UserModel()
        _user.uid = firebase_uid
        return cls.collection.get(_user.key)
