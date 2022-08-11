#  Project : KSRTC Seat Availability Notification System
#  Filename : admin.py
#  Author : thameem
#  Current modification time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
#  Last modified time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
import json

import requests
from beartype import beartype
from bs4 import BeautifulSoup
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from libs import authenticate
from main.settings import KSRTC_HOME_URL

from models import LocationModel


class Admin:

    @staticmethod
    @beartype
    def _fetch_locations() -> bool:
        response = requests.post(KSRTC_HOME_URL, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            raw_data = soup.find("main", attrs={"role": "main"}).find('script').string
            _locations = json.loads("".join(raw_data.split()).replace('varjsondata=', ""))
            _locations = list(filter(lambda x: x['id'], _locations))
            locations: list[LocationModel] = []
            for location in _locations:
                locations.append(
                    LocationModel.save_location(location_id=location['id'], location_name=location['value']))

            return True

        else:
            raise Exception(f"{response.status_code}")

    @staticmethod
    @beartype
    @authenticate
    def update_locations(request: WSGIRequest) -> 'HttpResponse':
        response = Admin._fetch_locations()
        if response is True:
            messages.success(request, 'Location update successful')
        else:
            messages.error(request, 'Location update failed')

        return redirect('/admin/locations/')

    @staticmethod
    @beartype
    @authenticate
    def dynamic_pages(request: WSGIRequest, page: str) -> 'HttpResponse':
        from models import LocationModel
        data = {'locations': LocationModel.get_all_locations(),
                'page_title': f"{request.session['user_name']} - {page.title()} | KSRTC Seat Availability Notification"}
        return render(request, f'admin/{page}.html', data)
