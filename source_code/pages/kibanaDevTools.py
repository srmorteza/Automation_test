from locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class KibanaDevTools:
    def __init__(self, driver):
        self.driver = driver

    def find_input(self):
        self.driver.find_element(By.XPATH, devtools_div_input_xpath).click()

    def click_enter(self):
        actions = ActionChains(driver=self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def write_query_input_textarea(self):
        query = self.driver.find_element(By.XPATH, devtools_textarea_input_xpath)
        actions = ActionChains(driver=self.driver)
        actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
        actions.key_up(Keys.CONTROL).perform()
        query.send_keys("GET automation/_search")
        actions.send_keys(Keys.ENTER).perform()
        query.send_keys("{")
        actions.send_keys(Keys.ENTER).perform()
        query.send_keys(' "query": {')
        actions.send_keys(Keys.ENTER).perform()
        query.send_keys(' "match" : {')
        actions.send_keys(Keys.ENTER).perform()
        query.send_keys('"_id":"XA_pWYMBwZNegVE_qIA-"')


    def run_query(self):
        self.driver.find_element(By.XPATH, query_execute_button_xpath).click()


class TestQuery:
    def __init__(self, driver):
        self.driver = driver

    def find_status_code(self):
        statuscode = self.driver.find_element(By.XPATH, output_statusCode_xpath)
        return statuscode

    def find_output_value(self):
        value =self.driver.find_element(By.XPATH, output_textarea_xpath)
        return value

