#  Project : KSRTC Seat Availability Notification System
#  Filename : ksrtc_service_locations.py
#  Author : blacklist
#  Current modification time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time
#  Last modified time : Sun, 17 Apr 2022 at 11:14 PM India Standard Time

import requests

from settings import KSRTC_HOME_URL


class KSRTCServiceLocations:

    @staticmethod
    def get_html_response():
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.get(KSRTC_HOME_URL, headers=headers)

    def get_ksrtc_service_locations(self) -> None:
        pass
