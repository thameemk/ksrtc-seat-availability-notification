#  Project : KSRTC Seat Availability Notification System
#  Filename : ksrtc_service_locations.py
#  Author : blacklist
#  Current modification time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time
#  Last modified time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time

import requests

from bs4 import BeautifulSoup

from settings import KSRTC_HOME_URL


class KSRTCServiceLocations:

    def __init__(self):
        r = requests.get(KSRTC_HOME_URL, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            a = soup
        else:
            raise Exception(f"{r.status_code} - {r.reason}")

    def get_ksrtc_service_locations(self) -> None:
        pass


if __name__ == '__main__':
    KSRTCServiceLocations()
