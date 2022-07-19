#  Project : KSRTC Seat Availability Notification System
#  Filename : authenticate.py
#  Author : thameem
#  Current modification time : Tue, 19 Jul 2022 at 9:26 AM India Standard Time
#  Last modified time : Tue, 19 Jul 2022 at 9:26 AM India Standard Time
from functools import wraps

from beartype import beartype


@beartype
def authenticate(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        # todo - context or session management
        if args.session['user'] is None:
            raise Exception("not logged in")
        else:
            return func(*args, **kwargs)

    return wrap
