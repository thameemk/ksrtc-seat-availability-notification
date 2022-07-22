#  Project : KSRTC Seat Availability Notification System
#  Filename : admin.py
#  Author : thameem
#  Current modification time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
#  Last modified time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
import json

import requests
from beartype import beartype
from bs4 import BeautifulSoup

from main.settings import KSRTC_HOME_URL

from app.models import LocationModel


class Admin:

    @staticmethod
    @beartype
    def _fetch_locations() -> list[LocationModel]:
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

            return locations

        else:
            raise Exception(f"{response.status_code}")
