#  Project : KSRTC Seat Availability Notification System
#  Filename : ksrtc_service_locations.py
#  Author : blacklist
#  Current modification time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time
#  Last modified time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time
import json
import re

import requests

from bs4 import BeautifulSoup

# from settings import KSRTC_HOME_URL

KSRTC_HOME_URL = "https://online.keralartc.com/oprs-web/"


class KSRTCServiceLocations:

    def __init__(self):
        r = requests.get(KSRTC_HOME_URL, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            locations = soup.find_all("script")[16].string
            # pattern = re.compile('var jsondata = (.*?);')
            pattern = re.search(r'jsondata\s*=\s*(.*?}])\s*\n', locations, flags=re.DOTALL)
            # m = pattern.match(locations)
            # stocks = json.loads(m.groups()[0])
            a = pattern
        else:
            raise Exception(f"{r.status_code} - {r.reason}")

    def get_ksrtc_service_locations(self) -> None:
        pass


if __name__ == '__main__':
    KSRTCServiceLocations()
