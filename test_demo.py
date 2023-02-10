from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from locators import element_locators
import pytest
import time
class test_login_page:
    driver =webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # constructor method class Suman
    def __init__(self):
        self.url = 'https://opensource-demo.orangehrmlive.com'
    # fetch the title of the webpage using Python Selenium
    def test_get_and_verify_title(self):
        self.driver.get(self.url)
        assert self.driver.title=='OrangeHRM'
        # return self.driver.title
    # fetch the URL of the webpage
    def test_get_and_verify_url(self):
        self.driver.get(self.url)
        assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        # return self.driver.current_url
    # fetch the entire content of the webpage
    def test_get_webpage(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self.driver.page_source
    def test_login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.NAME,value=element_locators.username_name).send_keys(element_locators.username)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=element_locators.password_name).send_keys(element_locators.password)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=element_locators.login_btn_xpath).click()
        time.sleep(1)
class_obj = test_login_page()
class_obj.test_get_and_verify_title()
# class_obj.test_get_and_verify_url()
# class_obj.test_get_webpage()
# class_obj.test_login()
class_obj.driver.quit()
