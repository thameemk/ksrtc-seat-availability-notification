#  Project : KSRTC Seat Availability Notification System
#  Filename : user.py
#  Author : thameem
#  Current modification time : Mon, 23 May 2022 at 12:05 AM India Standard Time
#  Last modified time : Mon, 23 May 2022 at 12:05 AM India Standard Time
import threading
import uuid
from datetime import datetime, date

from beartype import beartype
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.libs import authenticate
from app.models import NotificationModel, LocationModel, UserModel
from libs.get_services import GetServices


class User:

    @staticmethod
    @beartype
    @authenticate
    def dynamic_pages(request: WSGIRequest, page: str) -> 'HttpResponse':
        page_slugs_combined = " ".join(page.split("_"))
        data = {
            'page_title': f"{request.session['user_name']} - {page_slugs_combined.title()} | KSRTC Seat Availability "
                          f"Notification"}
        if page == 'add_notification':
            data['locations'] = LocationModel.get_all_locations()

        if page == 'notifications':
            data['notifications'] = NotificationModel.get_notifications(request.session['user'])

        return render(request, f'user/{page}.html', data)

    @staticmethod
    @beartype
    @authenticate
    def save_notification(request: WSGIRequest) -> 'HttpResponse':

        leaving_from = LocationModel.get_location_by_id(request.POST['leaving_from'])
        going_to = LocationModel.get_location_by_id(request.POST['going_to'])

        user = UserModel.get_user(firebase_uid=request.session['user'])

        date_of_departure = datetime.strptime(request.POST['date_of_departure'], "%Y-%m-%d")

        _notification_obj = NotificationModel(
            notification_id=uuid.uuid4().hex,
            leaving_from=leaving_from,
            going_to=going_to,
            date_of_departure=date_of_departure,
            date_of_return=datetime.strptime(request.POST['date_of_return'], "%Y-%m-%d") if request.POST[
                'date_of_return'] else None,
            user=user,
            available_seats=0,
            time_interval=int(request.POST['time_interval']),
        )

        notification = NotificationModel.save_notification(_notification_obj)

        threading.Thread(target=User._update_available_seats,
                         args=(request.POST['leaving_from'], request.POST['going_to'],
                               date_of_departure.date()))

        if notification:
            messages.success(request, 'Request in progress, please refresh the page to know the available seats')
        else:
            messages.error(request, 'Some sort of error has occurred.')

        return redirect('/user/add_notification')

    @staticmethod
    @beartype
    def _update_available_seats(notification: NotificationModel, leaving_from: str, going_to: str,
                                journey_date: date) -> None:

        available_seats = GetServices.get_total_seats(leaving_from, going_to, journey_date)
        notification.available_seats = available_seats
        notification.update()

    @staticmethod
    @beartype
    def disable_notification(request: WSGIRequest, notification_id: str) -> 'HttpResponse':
        notification_obj = NotificationModel.get_notification(request.session['user'], notification_id)
        notification_obj.is_active = False
        notification_obj.update()
        if notification_obj.is_active is False:
            messages.success(request, f'notification with id {notification_id} successfully disabled')
        else:
            messages.error(request, 'Some sort of error has occurred.')

        return redirect('/user/notifications/')

    @staticmethod
    @beartype
    def update_seats(request: WSGIRequest, notification_id: str) -> 'HttpResponse':
        notification_obj = NotificationModel.get_notification(request.session['user'], notification_id)

        if notification_obj:
            threading.Thread(target=User._update_available_seats,
                             args=(notification_obj.leaving_from.location_id, notification_obj.going_to.location_id,
                                   notification_obj.date_of_departure.date()))
            messages.success(request, 'Request in progress, please refresh the page to know the available seats')
        else:
            messages.error(request, 'Some sort of error has occurred.')

        return redirect('/user/notifications/')
