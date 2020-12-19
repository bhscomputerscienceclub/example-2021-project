from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

username = ''
password = ''

driver = Chrome()
driver.get("https://lgca.infinitecampus.org/campus/portal/students/beachwood.jsp")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_class_name('info').click()
cookies=driver.get_cookies()
driver.quit()

s = requests.Session()
for c in cookies:
    s.cookies[c['name']]= c['value']

r  = s.get('https://lgca.infinitecampus.org/campus/resources/portal/grades')
ic_grades = r.content.decode()