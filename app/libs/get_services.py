#  Project : KSRTC Seat Availability Notification System
#  Filename : get_services.py
#  Author : thameem
#  Current modification time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
#  Last modified time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
from datetime import date

import requests
from beartype import beartype
from bs4 import BeautifulSoup

from main.settings import POST_URL


class GetServices:

    @staticmethod
    @beartype
    def get_total_seats(leaving_from: str, going_to: str, journey_date: date) -> int:
        url = POST_URL

        url = url.replace('journey_date', journey_date.strftime('%d/%m/%Y'))
        url = url.replace('leaving_from', leaving_from)
        url = url.replace('going_to', going_to)

        response = requests.post(url=url, headers={'User-Agent': 'Mozilla/5.0'})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            seats_div = soup.find(id="fwTotalServicesId")
            try:
                total_seats = seats_div.text()
            except Exception:
                total_seats = 0
            return total_seats
        else:
            raise Exception(f"some error has been occurred on requesting services - {response.status_code}")
