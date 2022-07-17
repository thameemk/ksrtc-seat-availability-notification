#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Wed, 18 May 2022 at 11:50 PM India Standard Time
import logging
from datetime import datetime
from typing import Optional

from beartype import beartype
from fireo.fields import TextField, DateTime, BooleanField, IDField, NumberField
from fireo.models import Model


class UserModel(Model):
    class Meta:
        collection_name = "users"

    uid = IDField(required=True)
    full_name = TextField(required=True)
    phone_number = NumberField(required=True, int_only=True)
    is_deleted = BooleanField(required=True, default=False)
    created_on = DateTime(required=True, default=datetime.now())
    modified_on = DateTime(required=True, default=datetime.now())

    @classmethod
    @beartype
    def save_user(cls, firebase_uid: str, phone: int, full_name: str, ) -> 'UserModel':
        user_obj = UserModel(
            uid=firebase_uid,
            phone_number=phone,
            full_name=full_name
        ).save()
        return user_obj

    @classmethod
    @beartype
    def get_user(cls, firebase_uid: str) -> (bool, Optional['UserModel']):
        try:
            return True, UserModel.collection.get(key=firebase_uid)
        except Exception as e:
            logging.error(str(e))
            return False, None
