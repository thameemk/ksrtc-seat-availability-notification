#  Project : KSRTC Seat Availability Notification System
#  Filename : urls.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Mon, 16 May 2022 at 11:00 PM India Standard Time

from django.urls import path

from views import index, Login, User

urlpatterns = [
    path('', index, name='index'),
    path('login', Login.login, name='login'),
    path('user/home', User().home)

]
