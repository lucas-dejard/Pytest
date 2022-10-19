import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestContact:
    """Test the Link for ways to contact site"""

    def test_email(self):
        drivern = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//a[normalize-space()="Contact Us"]')
        time.sleep(3)
        drivern.quit()
        return "True"

    def test_about(self):
        drivere = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drivere.get("http://testphp.vulnweb.com/login.php")
        clicknumbere = drivere.find_element(By.XPATH, '//a[normalize-space()="About Us"]').click()
        time.sleep(3)
        drivere.quit()
        return "True"

    def test_privacy(self):
        drivere = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drivere.get("http://testphp.vulnweb.com/login.php")
        clicknumbere = drivere.find_element(By.XPATH, '//a[normalize-space()="Privacy Policy"]').click()
        time.sleep(3)
        drivere.quit()
        return "True"


class TestRegister:
    """Test Register Page"""

    def test_signup(self):
        global drivern, clicknumbern
        drivern = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
        clicknumbern = drivern.find_element(By.XPATH, "//textarea[@name='uaddress']").send_keys(
            "rua do fim do mundo, 000")
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
        drivern = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//input[@name="uname"]').send_keys("testefalha@gmail.com")
        time.sleep(3)
        return "True"

    def test_password_false(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='pass']").send_keys("testefalha@gmail.com")
        time.sleep(3)
        return "True"

    def test_login_click_false(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@value='login']").click()
        time.sleep(3)
        return "True"
    def test_verify_false(self):
        clicknumbern = drivern.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/h3[1]/font[1]")
        time.sleep(3)
        drivern.quit()
        return "True"

class TestLogin:
    """Test with right inputs to log in"""

    def test_login(self):
        global drivern, clicknumbern
        drivern = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        drivern.get("http://testphp.vulnweb.com/login.php")
        clicknumbern = drivern.find_element(By.XPATH, '//input[@name="uname"]').send_keys("test")
        time.sleep(3)
        return "True"

    def test_password(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='pass']").send_keys("test")
        time.sleep(3)
        return "True"

    def test_login_click(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@value='login']").click()
        time.sleep(3)
        return "True"
    def test_verify_login(self):
        clicknumbern = drivern.find_element(By.XPATH, "//input[@name='update']")
        print(clicknumbern)
        return "True"

