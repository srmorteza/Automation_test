from locator import *
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, password_textbox_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, login_button_xpath).click()

    def dashboard_check(self):
        self.driver.find_element(By.XPATH, dashboard_label_xpath)