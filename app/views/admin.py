#  Project : KSRTC Seat Availability Notification System
#  Filename : admin.py
#  Author : thameem
#  Current modification time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
#  Last modified time : Fri, 22 Jul 2022 at 12:22 AM India Standard Time
import json

import requests
from bs4 import BeautifulSoup

from main.settings import KSRTC_HOME_URL


class Admin:

    @staticmethod
    def _fetch_locations():
        response = requests.post(KSRTC_HOME_URL, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            raw_data = soup.find("main", attrs={"role": "main"}).find('script').string
            locations = json.loads("".join(raw_data.split()).replace('varjsondata=', ""))
            print(locations)
        else:
            raise Exception(f"{response.status_code}")
