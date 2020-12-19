from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

driver = Chrome()
driver.get("https://www.sbgbook.xyz/gbook/login/")
username = ''
password = ''
driver.find_element_by_class_name("btn-success").click()
time.sleep(1)
driver.find_element_by_id('id_LogIn-username').send_keys(username)
driver.find_element_by_id('id_LogIn-password').send_keys(password)
driver.find_element_by_id('lgnbtn').click()
url = driver.current_url
cookies=driver.get_cookies()
driver.quit()

s = requests.Session()
for c in cookies:
    s.cookies[c['name']]= c['value']
#still need to get sectionid, studentid, and collectionid from url
r  = s.post('https://www.sbgbook.xyz/gbook/studentgradeframe/?section_id=796&student_id=5117&scollection_id=1013')
sbg_grades = r.content.decode()