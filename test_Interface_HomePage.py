import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class Test_Contact:
    """Test the Link for ways to contact site"""
    def test_email(self):
        drivern = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//a[normalize-space()="Contact Us"]')
        time.sleep(3)
        drivern.quit()
        return "True"

    """Test the Link for E-mail"""
    def test_number(self):
        drivere = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivere.get("http://testphp.vulnweb.com/login.php")
        clicknumbere = drivere.find_element(By.XPATH, '//a[normalize-space()="About Us"]').click()
        time.sleep(6)
        drivere.quit()
        return "True"


class Test_login_false:
    """Test with wrong inputs to Fail"""
    def test_login_false(self):
        global drivern, clicknumbern
        drivern = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//input[@name="uname"]').send_keys("testefalha@gmail.com")
        time.sleep(3)
        return "True"

    def test_password_false(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='pass']").send_keys("testefalha@gmail.com")
        time.sleep(3)
        drivern.quit()
        return "True"