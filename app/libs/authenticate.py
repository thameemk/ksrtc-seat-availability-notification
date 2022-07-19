#  Project : KSRTC Seat Availability Notification System
#  Filename : authenticate.py
#  Author : thameem
#  Current modification time : Tue, 19 Jul 2022 at 9:26 AM India Standard Time
#  Last modified time : Tue, 19 Jul 2022 at 9:26 AM India Standard Time
from functools import wraps

from beartype import beartype
from django.shortcuts import redirect


# flake8: noqa ANN001, ANN201, ANN002, ANN003
@beartype
def authenticate(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        # todo - context or session management
        if 'user' in args[0].session:
            return func(*args, **kwargs)
        else:
            return redirect('login')

    return wrap
