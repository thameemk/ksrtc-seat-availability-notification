#  Project : KSRTC Seat Availability Notification System
#  Filename : firebase_auth.py
#  Author : thameem
#  Current modification time : Wed, 25 May 2022 at 12:15 AM India Standard Time
#  Last modified time : Wed, 25 May 2022 at 12:15 AM India Standard Time
import logging

import firebase_admin
from beartype import beartype
from firebase_admin import auth


class FirebaseAuth:
    @beartype
    def __init__(self) -> None:
        try:
            firebase_admin.initialize_app()
        except Exception as e:
            logging.error(str(e))
            firebase_admin.get_app()

    @beartype
    def validate_token(self, id_token: str) -> dict:
        return auth.verify_id_token(id_token)
