#  Project : KSRTC Seat Availability Notification System
#  Filename : urls.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:06 PM India Standard Time
#  Last modified time : Mon, 16 May 2022 at 11:00 PM India Standard Time

from django.urls import path

from app.views import Login, User, Admin

urlpatterns = [
    path('', Login.login),
    path('login', Login.login, name='login'),
    path('auth/logout/', Login.logout),
    path('auth/callback/', Login.auth_callback),

    path('user/save_notification/', User.save_notification),

    path('admin/<page>/', Admin.dynamic_pages),
    path('user/<page>/', User.dynamic_pages),


]
