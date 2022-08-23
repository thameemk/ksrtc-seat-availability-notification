#  Project : KSRTC Seat Availability Notification System
#  Filename : get_services.py
#  Author : thameem
#  Current modification time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
#  Last modified time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
import requests
from beartype import beartype

from main.settings import POST_URL


class GetServices:

    @staticmethod
    @beartype
    def post(leaving_from: str, going_to: str, journey_date: str) -> None:
        url = POST_URL

        url = url.replace('journey_date', journey_date)
        url = url.replace('leaving_from', leaving_from)
        url = url.replace('going_to', going_to)

        response = requests.post(url=url, headers={'User-Agent': 'Mozilla/5.0'})

        if response.status_code == 200:
            pass
        else:
            raise Exception(f"some error has been occurred on requesting services - {response.status_code}")


if __name__ == '__main__':
    GetServices().post(leaving_from="1540487668225",
                       going_to="1540485175138",
                       journey_date='28/08/2022')
