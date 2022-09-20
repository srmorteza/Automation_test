from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.login import Login
from pages.kibanaDevTools import KibanaDevTools, TestQuery

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(6)

# open the website
driver.get("http://localhost:5601/login?next=%2F")
login = Login(driver=driver)
login.enter_username('elastic')
login.enter_password('9ga9lGgIXlEXL7=j3AtG')
login.click_on_login_button()
sleep(3)
login.dashboard_check()
sleep(2)
driver.get("http://localhost:5601/app/dev_tools#/console")
kibana = KibanaDevTools(driver=driver)
kibana.find_input()
kibana.click_enter()
kibana.write_query_input_textarea()
sleep(1)
kibana.run_query()
sleep(1)

output = TestQuery(driver=driver)
statusCode = output.find_status_code()

if statusCode.text == '200 - OK':
    print("status code is  200 and  query is ok")
    value = output.find_output_value()
    if 'Automation test - ayatollahi' in value.text:
        print('sucssess !!! teat is pass ')
    else:
        print('test is fail')
