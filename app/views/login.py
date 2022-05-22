#  Project : KSRTC Seat Availability Notification System
#  Filename : login.py
#  Author : thameem
#  Current modification time : Thu, 19 May 2022 at 8:22 PM India Standard Time
#  Last modified time : Thu, 19 May 2022 at 8:22 PM India Standard Time
from django.http import HttpResponse
from django.shortcuts import render


class Login:
    @staticmethod
    def login_action(request):
        phone_number = request.POST.get('phone_number')
        return HttpResponse(f"Connection Successful")

    @staticmethod
    def login(request):
        data = {'page_title': 'Login | KSRTC Seat Availability Notification'}
        return render(request, 'login.html', data)
