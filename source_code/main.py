import queue
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(6)

# open the website
driver.get("http://localhost:5601/login?next=%2F")
# sleep(1)

# click on photo of menu and show
username = driver.find_element(By.XPATH, '//input[@name="username"]')
username.click()
username.clear()
username.send_keys('elastic')
# sleep(1)

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.click()
password.clear()
password.send_keys('9ga9lGgIXlEXL7=j3AtG')
# sleep(1)


driver.find_element(By.XPATH, '//button[@class="euiButton euiButton--primary euiButton--fill"]').click()

# click on iphone and showls
# driver.find_element(By.XPATH, '//a[text()="iPhone"]').click()
sleep(3)

driver.find_element(By.XPATH, '//h1[text()="Welcome home"]')
# print("find welcome")
sleep(3)




driver.get("http://localhost:5601/app/dev_tools#/console")

code = driver.find_element(By.XPATH, '//div[@class="ace_content"]')
code.click()
actions.send_keys(Keys.ENTER).perform()




query = driver.find_element(By.XPATH, '//textarea[@class="ace_text-input"]')
# query.click()
actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
actions.key_up(Keys.CONTROL).perform()

# query.send_keys("GET .ds-logs-generic-default-2022.09.18-000001/_search { 'query': { 'match' : {"
#                 "'_id':'EOfaT4MB-0ya7ag5VPYg'' }}}")

# str='GET automation/_search\r{\r"query": {\r "match" : {\r "_id":"XA_pWYMBwZNegVE_qIA-" \r }\r}'
# query.send_keys(str)
# actions.send_keys(Keys.ENTER).perform()
# query.send_keys('}')

query.send_keys("GET automation/_search")
actions.send_keys(Keys.ENTER).perform()
query.send_keys("{")
actions.send_keys(Keys.ENTER).perform()

query.send_keys(' "query": {')
actions.send_keys(Keys.ENTER).perform()

query.send_keys(' "match" : {')
actions.send_keys(Keys.ENTER).perform()

query.send_keys('"_id":"XA_pWYMBwZNegVE_qIA-"')
actions.send_keys(Keys.ENTER).perform()

query.send_keys('}')
actions.send_keys(Keys.ENTER).perform()

query.send_keys('}')
actions.send_keys(Keys.ENTER).perform()

query.send_keys('}')

driver.find_element(By.XPATH, '//button[@class="euiLink css-pqycxy-euiLink-success"]').click()
sleep(2)


statusCode = driver.find_element(By.XPATH, '//span[@class="euiBadge__text"]')
# print(statusCode.text)
if statusCode.text == '200 - OK':
    print("tatus code in  200 and  query is ok")
else:
    print("not ok" + statusCode.text)



outputCode = driver.find_element(By.XPATH, '//div[@class="conApp__output ace_editor ace-tm"]')
output = outputCode.text

if 'Automation test - ayatollahi' in output:
    print('sucssess !!!! ')
else:
    print('test is fail')


driver.close()
