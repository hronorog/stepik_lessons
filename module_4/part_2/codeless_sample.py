# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test123():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_123(self):
        self.driver.get("http://selenium1py.pythonanywhere.com/ru/")
        self.driver.find_element(By.ID, "logout_link").click()
        self.driver.find_element(By.ID, "login_link").click()
        self.driver.find_element(By.ID, "id_registration-email").click()
        self.driver.find_element(By.ID, "id_registration-email").send_keys("sdkttfjs@mail.ru")
        self.driver.find_element(By.ID, "id_registration-password1").send_keys("123456789Zz!")
        self.driver.find_element(By.ID, "id_registration-password2").click()
        self.driver.find_element(By.ID, "id_registration-password2").send_keys("123456789Zz!")
        self.driver.find_element(By.NAME, "registration_submit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".alert").click()

