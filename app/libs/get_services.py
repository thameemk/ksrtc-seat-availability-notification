#  Project : KSRTC Seat Availability Notification System
#  Filename : get_services.py
#  Author : thameem
#  Current modification time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
#  Last modified time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
import time

from beartype import beartype
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from main.settings import KSRTC_HOME_URL


class GetServices:

    def __init__(self) -> None:
        self.driver = None

    @beartype
    def _set_location(self, location: str, location_key: str, location_response_key: str) -> None:
        time.sleep(3)
        location_info = self.driver.find_element(By.ID, location_key)
        location_info.send_keys(location)
        time.sleep(3)
        self.driver.find_elements(By.ID, location_response_key)[0].click()

    @beartype
    def _set_journey_date(self, date: str, date_key: str) -> None:
        time.sleep(3)
        calendar = self.driver.find_element(By.ID, date_key)
        # calendar = self.driver.find_element(By.XPATH, "/html/body/div[6]/table/tbody/tr[2]/td[4]")
        calendar.click()
        calendar.send_keys(date)
        time.sleep(3)

    @beartype
    def post(self, leaving_from: str, going_to: str, journey_date: str) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(KSRTC_HOME_URL)

        self._set_location(leaving_from, 'fromPlaceName', 'ui-id-3')
        self._set_location(going_to, 'toPlaceName', 'ui-id-4')
        self._set_journey_date(journey_date, 'txtJourneyDate')

        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        response = self.driver.page_source

        print(response)


if __name__ == '__main__':
    GetServices().post(leaving_from="TRIVANDRUM",
                       going_to="KOZHIKODE",
                       journey_date='28/08/2022')
