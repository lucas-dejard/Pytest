import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class Test_Contact:
    """Test the Link for Telephone Number"""
    def test_number(self):
        drivern = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivern.get("https://www.phptravels.net/login")
        clicknumbern = drivern.find_element(By.XPATH, '//a[normalize-space()="+1-234-56789"]').click
        time.sleep(3)
        drivern.quit()
        return "True"

    """Test the Link for E-mail"""
    def test_email(self):
        drivere = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivere.get("https://www.phptravels.net/login")
        clicknumbere = drivere.find_element(By.XPATH, '//ul[@class="list-items"]//a[contains(@class,"waves-effect")]'
                                                      '[normalize-space()="info@travelagency.com"]').click
        time.sleep(3)
        drivere.quit()
        return "True"




