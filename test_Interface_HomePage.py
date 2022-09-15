import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class TestContact:
    """Test the Link for ways to contact site"""

    def test_email(self):
        drivern = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//a[normalize-space()="Contact Us"]')
        time.sleep(3)
        drivern.quit()
        return "True"

    def test_abt(self):
        drivere = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivere.get("http://testphp.vulnweb.com/login.php")
        clicknumbere = drivere.find_element(By.XPATH, '//a[normalize-space()="About Us"]').click()
        time.sleep(3)
        drivere.quit()
        return "True"


class TestRegister:
    """Test Register Page"""

    def test_signup(self):
        global drivern, clicknumbern
        drivern = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, "//a[normalize-space()='signup here']").click()
        time.sleep(3)
        return "True"

    def test_user(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='uuname']").send_keys("usernametest")
        time.sleep(3)
        return "True"

    def test_pass(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='upass']").send_keys("passwordtest")
        time.sleep(3)
        return "True"

    def test_pass_retype(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='upass2']").send_keys("passwordtest")
        time.sleep(3)
        return "True"

    def test_name(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='urname']").send_keys("nametest")
        time.sleep(3)
        return "True"

    def test_card(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='ucc']").send_keys("123876456098")
        time.sleep(3)
        return "True"

    def test_email(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='uemail']").send_keys("emailtest@gmail.com")
        time.sleep(3)
        return "True"

    def test_phone(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='uphone']").send_keys("40028922")
        time.sleep(3)
        return "True"

    def test_address(self):
        clicknumbern = drivern.find_element(By.XPATH, "//textarea[@name='uaddress']").send_keys("rua do fim do mundo, 000")
        time.sleep(3)
        return "True"

    def test_login_click(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='signup']").click()
        time.sleep(3)
        drivern.quit()
        return "True"


class TestLoginFalse:
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
        return "True"

    def test_login_click(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@value='login']").click()
        time.sleep(3)
        drivern.quit()
        return "True"

