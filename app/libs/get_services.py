#  Project : KSRTC Seat Availability Notification System
#  Filename : get_services.py
#  Author : thameem
#  Current modification time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
#  Last modified time : Mon, 15 Aug 2022 at 7:52 pm India Standard Time
import time

from beartype import beartype
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as ec

from main.settings import KSRTC_HOME_URL


class GetServices:

    @beartype
    def post(self, leaving_from: str, going_to: str, journey_date: str) -> None:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get(KSRTC_HOME_URL)

        wait = WebDriverWait(driver, 15)
        wait.until(ec.element_to_be_clickable((By.NAME, "startPlaceId"))).send_keys(leaving_from)

        # driver.find_element(By.NAME, 'startPlaceId').send_keys('value', leaving_from)
        # driver.find_elements(By.ID, "ui-id-3")[0].click()
        time.sleep(3)
        driver.find_element(By.ID, 'endPlaceId').send_keys("TRIVANDRUM")
        time.sleep(3)
        driver.find_element(By.ID, 'txtJourneyDate').send_keys(journey_date)
        time.sleep(3)
        driver.find_element(By.ID, 'searchBtn').click()
        time.sleep(5)
        response = BeautifulSoup(driver.page_source, 'html.parser')

        print(response.prettify())


if __name__ == '__main__':
    GetServices().post(leaving_from="1540487668225",
                       going_to="1540485175138",
                       journey_date='28/08/2022')
