#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Mon, 23 May 2022 at 12:05 AM India Standard Time
#  Last modified time : Mon, 23 May 2022 at 12:05 AM India Standard Time
from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.libs import authenticate
from models import NotificationModel, LocationModel


class User:

    @staticmethod
    @beartype
    @authenticate
    def dynamic_pages(request: WSGIRequest, page: str) -> 'HttpResponse':
        data = {'page_title': f"{request.session['user_name']} - {page.title()} | KSRTC Seat Availability Notification",
                'notifications': NotificationModel.get_notifications(request.session['user'])}
        return render(request, f'user/{page}.html', data)

    @staticmethod
    @beartype
    @authenticate
    def save_notification(request: WSGIRequest) -> 'HttpResponse':

        leaving_from = LocationModel.get_location_by_id(request.POST['leaving_from'])
        going_to = LocationModel.get_location_by_id(request.POST['going_to'])

        _notification_obj = NotificationModel(
            leaving_from=leaving_from,
            going_to=going_to,
            date_of_departure=request.POST['date_of_departure'],
            date_of_return=request.POST['date_of_return'],
            user=request.session['user'],
            time_interval=request.POST['time_interval'],
            receive_notification_up_to=request.POST['receive_notification_up_to'],
        )

        notification = NotificationModel.save_notification(_notification_obj)

        if notification:
            pass
        else:
            pass

        return redirect('user/add_notification')
